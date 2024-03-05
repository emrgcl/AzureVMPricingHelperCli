
import json
import urllib.request as request
import yaspin

@yaspin.yaspin(text="Fetching Azure VM SKUs")
def fetch_virtual_machine_sku_prices(virtual_machine_calculator_api='https://azure.microsoft.com/api/v3/pricing/virtual-machines/calculator/?culture=en-us&currency=$currency'):
        try:
            response=request.urlopen(virtual_machine_calculator_api)
            data = response.read()
            jsondata = json.loads(data)
            return jsondata
        except Exception as e:
            print(f"Error occurred while fetching virtual machine prices: {e}")
def get_vm_spec_ratio(size):
     ratio = {
          "f" : { 'cpu_ram_ratio': 2,'ram_disk_ratio' : 8},
          "fs" : { 'cpu_ram_ratio': 1.0,'ram_disk_ratio' : 2},
          "fsv2" : { 'cpu_ram_ratio': 2,'ram_disk_ratio' : 4},
          "fx" : { 'cpu_ram_ratio': 21,'ram_disk_ratio' :2},
     }
     return ratio[size]