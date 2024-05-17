from string import printable
import requests

def get_location_ipinfo(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
        data = response.json()
        return {
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": data.get("loc"),
            "Org": data.get("org"),
            "Postal": data.get("postal"),
            "Timezone": data.get("timezone")
        }
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def get_location_ipstack(ip_address, api_key):
    try:
        response = requests.get(f"http://api.ipstack.com/{ip_address}?access_key={api_key}")
        response.raise_for_status()
        data = response.json()
        return {
            "City": data.get("city"),
            "Region": data.get("region_name"),
            "Country": data.get("country_name"),
            "Location": f"{data.get('latitude')},{data.get('longitude')}",
            "Org": data.get("organisation"),
            "Postal": data.get("zip"),
            "Timezone": data.get("time_zone", {}).get("id")
        }
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def get_location_ipgeolocation(ip_address, api_key):
    try:
        response = requests.get(f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip_address}")
        response.raise_for_status()
        data = response.json()
        return {
            "City": data.get("city"),
            "Region": data.get("state_prov"),
            "Country": data.get("country_name"),
            "Location": f"{data.get('latitude')},{data.get('longitude')}",
            "Org": data.get("isp"),
            "Postal": data.get("zipcode"),
            "Timezone": data.get("time_zone", {}).get("name")
        }
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def get_location_ipapi(ip_address):
    try:
        response = requests.get(f"https://ipapi.co/{ip_address}/json/")
        response.raise_for_status()
        data = response.json()
        return {
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country_name"),
            "Location": f"{data.get('latitude')},{data.get('longitude')}",
            "Org": data.get("org"),
            "Postal": data.get("postal"),
            "Timezone": data.get("timezone")
        }
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def get_location_ipapi_com(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        response.raise_for_status()
        data = response.json()
        return {
            "City": data.get("city"),
            "Region": data.get("regionName"),
            "Country": data.get("country"),
            "Location": f"{data.get('lat')},{data.get('lon')}",
            "Org": data.get("isp"),
            "Postal": data.get("zip"),
            "Timezone": data.get("timezone")
        }
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def get_location_extreme_ip_lookup(ip_address):
    try:
        response = requests.get(f"https://extreme-ip-lookup.com/json/{ip_address}")
        response.raise_for_status()
        data = response.json()
        return {
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": f"{data.get('lat')},{data.get('lon')}",
            "Org": data.get("isp"),
            "Timezone": data.get("timezone")
        }
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def get_location_ipdata(ip_address, api_key):
    try:
        response = requests.get(f"https://api.ipdata.co/{ip_address}?api-key={api_key}")
        response.raise_for_status()
        data = response.json()
        return {
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country_name"),
            "Location": f"{data.get('latitude')},{data.get('longitude')}",
            "Org": data.get("organisation"),
            "Postal": data.get("postal"),
            "Timezone": data.get("time_zone", {}).get("name")
        }
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def get_location_ipwhois(ip_address):
    try:
        response = requests.get(f"https://ipwhois.app/json/{ip_address}")
        response.raise_for_status()
        data = response.json()
        return {
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": f"{data.get('latitude')},{data.get('longitude')}",
            "Org": data.get("isp"),
            "Postal": data.get("postal"),
            "Timezone": data.get("timezone")
        }
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def get_location_ipfind(ip_address, api_key):
    try:
        response = requests.get(f"https://ipfind.co/?ip={ip_address}&auth={api_key}")
        response.raise_for_status()
        data = response.json()
        return {
            "City": data.get("city"),
            "Region": data.get("region"),
            "Country": data.get("country"),
            "Location": f"{data.get('latitude')},{data.get('longitude')}",
            "Org": data.get("organisation"),
            "Timezone": data.get("timezone")
        }
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def get_location_ip2location(ip_address, api_key):
    try:
        response = requests.get(f"https://api.ip2location.com/v2/?ip={ip_address}&key={api_key}&package=WS24&format=json")
        response.raise_for_status()
        data = response.json()
        return {
            "City": data.get("city_name"),
            "Region": data.get("region_name"),
            "Country": data.get("country_name"),
            "Location": f"{data.get('latitude')},{data.get('longitude')}",
            "Org": data.get("isp"),
            "Timezone": data.get("time_zone")
        }
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

def print_table(location_info):
    print("+-------------+-------------+------------+--------------+--------------+--------+-----------+")
    print("| City        | Region      | Country    | Location     | Org          | Postal | Timezone  |")
    print("+-------------+-------------+------------+--------------+--------------+--------+-----------+")
    for item in location_info:
        city = item.get('City', 'Bilinmiyor') if item.get('City') else 'Bilinmiyor'
        region = item.get('Region', 'Bilinmiyor') if item.get('Region') else 'Bilinmiyor'
        country = item.get('Country', 'Bilinmiyor') if item.get('Country') else 'Bilinmiyor'
        location = item.get('Location', 'Bilinmiyor') if item.get('Location') else 'Bilinmiyor'
        org = item.get('Org', 'Bilinmiyor') if item.get('Org') else 'Bilinmiyor'
        postal = item.get('Postal', 'Bilinmiyor') if item.get('Postal') else 'Bilinmiyor'
        timezone = item.get('Timezone', 'Bilinmiyor') if item.get('Timezone') else 'Bilinmiyor'

        print(f"| {city:<12} | {region:<12} | {country:<10} | {location:<12} | {org:<12} | {postal:<6} | {timezone:<9} |")
    print("+-------------+-------------+------------+Krmatlgn--------------+--------------+--------+-----------+")
print("+-------------+-------------+------------+https://github.com/Krmatlgn/IpLocation--------------+--------------+--------+-----------+")



def main():
    ip_address = input("Lütfen bir IP adresi girin: ")

    ipstack_api_key = "YOUR_IPSTACK_API_KEY" 
    ipgeolocation_api_key = "YOUR_IPGEOLOCATION_API_KEY" 
    ipdata_api_key = "YOUR_IPDATA_API_KEY"  
    ipfind_api_key = "YOUR_IPFIND_API_KEY" 
    ip2location_api_key = "YOUR_IP2LOCATION_API_KEY"  

    location_info = []

    sources = [
        get_location_ipinfo,
        lambda ip: get_location_ipstack(ip, ipstack_api_key),
        lambda ip: get_location_ipgeolocation(ip, ipgeolocation_api_key),
        get_location_ipapi,
        get_location_ipapi_com,
        get_location_extreme_ip_lookup,
        lambda ip: get_location_ipdata(ip, ipdata_api_key),
        get_location_ipwhois,
        lambda ip: get_location_ipfind(ip, ipfind_api_key),
        lambda ip: get_location_ip2location(ip, ip2location_api_key)
    ]

    for source in sources:
        try:
            result = source(ip_address)
            location_info.append(result)
        except Exception as e:
            print(f"Hata: {e}")

    print_table(location_info)

if __name__ == "__main__":
    main()

