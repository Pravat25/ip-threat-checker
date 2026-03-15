import requests

ip = input("Enter IP address to check: ")

url = f"http://ip-api.com/json/{ip}"

response = requests.get(url)

data = response.json()

print("\n===== IP Intelligence Report =====\n")

print("IP:", data.get("query"))
print("Country:", data.get("country"))
print("Region:", data.get("regionName"))
print("ISP:", data.get("isp"))

if data.get("proxy") or data.get("hosting"):
    print("⚠️ Potentially suspicious IP")
else:
    print("No obvious threat indicators")
