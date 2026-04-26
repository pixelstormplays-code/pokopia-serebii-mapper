import requests
from bs4 import BeautifulSoup

# ==========================================
# POKOPIA BLUEPRINT NEXUS - CORE ENGINE
# "Your point being? The math works."
# ==========================================

class NexusScraper:
    def __init__(self):
        self.url = "https://www.serebii.net/pokemonpokopia/items.shtml"
        self.headers = {'User-Agent': 'PokopiaBlueprintNexus-Bot/1.0'}

    def get_peak_data(self):
        """
        Rips the item list from Serebii to fuel the optimizer.
        """
        print(f"📡 Connecting to the Serebii Nexus...")
        
        try:
            response = requests.get(self.url, headers=self.headers)
            # If Serebii tries to stop us... Nuh Uh.
            response.raise_for_status() 
            
            soup = BeautifulSoup(response.text, 'html.parser')
            items_found = []

            # Targeting the 'dextable' class which Serebii usually uses
            tables = soup.find_all('table', class_='dextable')
            
            for table in tables:
                rows = table.find_all('tr')
                for row in rows[1:]: # Skip headers
                    cells = row.find_all('td')
                    if cells:
                        item_name = cells[0].get_text(strip=True)
                        items_found.append(item_name)

            print(f"✅ Success. {len(items_found)} items imported into the Brain.")
            return items_found

        except Exception as e:
            print(f"❌ Error: Could not reach the doorstep. Check your connection. {e}")
            return []

if __name__ == "__main__":
    brain = NexusScraper()
    item_list = brain.get_peak_data()
    
    # Proof of concept: List the first 5 items to show it works.
    print("\n[Preview of Optimal Materials]:")
    for item in item_list[:5]:
        print(f"- {item}")
      
