# 1. Create a list of tuples containing city names and their (latitude, longitude)
cities = [
    ("Paris", (48.8566, 2.3522)),
    ("New York", (40.7128, -74.0060)),
    ("Tokyo", (35.6895, 139.6917)),
    ("Cairo", (30.0444, 31.2357)),
    ("Sydney", (-33.8688, 151.2093))
]

# 2. Display each city with its coordinates
print("City coordinates:")
for city in cities:
    name = city[0]                # Extract city name
    coordinates = city[1]         # Extract (latitude, longitude) tuple
    print(f"{name}: {coordinates}")

# 3. Display only the latitudes of each city
print("\nLatitudes of cities:")
for city in cities:
    latitude = city[1][0]         # Get the first element of the coordinates tuple (latitude)
    print(latitude)

# 4. Calculate and display the mean latitude
latitudes = [city[1][0] for city in cities]  # Create a list of just the latitudes
mean_latitude = sum(latitudes) / len(latitudes)  # Calculate the average
print(f"\nMean latitude: {mean_latitude:.4f}")  # Display with 4 decimal places
