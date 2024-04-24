import requests


def get_university_rankings(country):

    try:
        url = "http://universities.hipolabs.com/search"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            universities = [university["name"] for university in data[:50]]
            return universities
        
        else:
            print(f"Error")
            return []
        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []



us_universities = get_university_rankings("United States")
uk_universities = get_university_rankings("United Kingdom")

print("United States Universities:")
for university in us_universities:
    print(university)

print("\nUnited Kingdom Universities:")
for university in uk_universities:
    print(university)
