# Make an empty list for storing aliens.
aliens = []

# Make 30 green ailens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 ailens
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many ailens have been created.
print(f"Total number of ailens: {len(aliens)}")