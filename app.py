import streamlit as st
import random
import json
import os

# Define the films
films = {
    'critically acclaimed': [
        'L.A. Confidential (1997)',  # 99%
        'The Godfather (1972)',  # 97%
        'Casablanca (1942)',  # 99%
        'Seven Samurai (1954)',  # 100%
        'Parasite (2019)',  # 99%
        'Schindler\'s List (1993)',  # 98%
        'Top Gun: Maverick (2022)',  # 96%
        'Toy Story 2 (1999)',  # 100%
        'Chinatown (1974)',  # 98%
        'On the Waterfront (1954)',  # 99%
        'The Battle of Algiers (1966)',  # 99%
        'Toy Story (1995)',  # 100%
        'Rear Window (1954)',  # 98%
        'Modern Times (1936)',  # 98%
        'How to Train Your Dragon (2010)',  # 99%
        'All About Eve (1950)',  # 99%
        'Spirited Away (2001)',  # 96%
        'Up (2009)',  # 98%
        'The Third Man (1949)',  # 99%
        'Spotlight (2015)',  # 97%
        'Spider-Man: Into the Spider-Verse (2018)',  # 97%
        'The Philadelphia Story (1940)',  # 100%
        'Finding Nemo (2003)',  # 99%
        'Singin\' in the Rain (1952)',  # 100%
        '12 Angry Men (1957)',  # 100%
        'Toy Story 3 (2010)',  # 98%
        'Sunset Boulevard (1950)',  # 98%
        'Coco (2017)',  # 97%
        'The Godfather, Part II (1974)',  # 96%
        'Three Colors: Red (1994)',  # 100%
        'Selma (2014)',  # 99%
        'Zootopia (2016)',  # 98%
        'Citizen Kane (1941)',  # 99%
        'Annie Hall (1977)',  # 97%
        'Cool Hand Luke (1967)',  # 100%
        'The Holdovers (2023)',  # 97%
        'Inside Out (2015)',  # 98%
        'Dr. Strangelove Or: How I Learned to Stop Worrying and Love the Bomb (1964)',  # 98%
        'Let the Right One In (2008)',  # 98%
        'The Lord of the Rings: The Two Towers (2002)',  # 95%
        'Knives Out (2019)',  # 97%
        'M (1931)',  # 100%
        'Toy Story 4 (2019)',  # 97%
        'The Wrestler (2008)',  # 99%
        'Goodfellas (1990)',  # 94%
        'The Wizard of Oz (1939)',  # 98%
        'Double Indemnity (1944)',  # 97%
        'Psycho (1960)',  # 97%
        'Paddington 2 (2017)',  # 99%
        'Before Sunrise (1995)',  # 100%
        'The Dark Knight (2008)',  # 94%
        'The Maltese Falcon (1941)',  # 99%
        'It Happened One Night (1934)',  # 98%
        'The Wages of Fear (1953)',  # 100%
        'North by Northwest (1959)',  # 97%
        'Bicycle Thieves (1948)',  # 99%
        'Alien (1979)',  # 93%
        'Argo (2012)',  # 96%
        'Get Out (2017)',  # 98%
        'The Kid (1921)',  # 100%
        'Mission: Impossible - Dead Reckoning Part One (2023)',  # 96%
        'The Pianist (2002)',  # 95%
        'Kind Hearts and Coronets (1949)',  # 100%
        'The 400 Blows (1959)',  # 99%
        'Grave of the Fireflies (1988)',  # 100%
        'The Big Sick (2017)',  # 98%
        'Minari (2020)',  # 98%
        'Portrait of a Lady on Fire (2019)',  # 97%
        'The Treasure of the Sierra Madre (1948)',  # 100%
        'Apocalypse Now (1979)',  # 90%
        'Mission: Impossible - Fallout (2018)',  # 98%
        'The Last Picture Show (1971)',  # 98%
        'Tampopo (1985)',  # 100%
        'Mad Max: Fury Road (2015)',  # 97%
        'Tokyo Story (1953)',  # 100%
        'A Hard Day\'s Night (1964)',  # 98%
        'Metropolis (1927)',  # 97%
        'Good Will Hunting (1997)',  # 97%
        'The Gold Rush (1925)',  # 100%
        'Aliens (1986)',  # 94%
        'Spider-Man: Across the Spider-Verse (2023)',  # 95%
        'The Good, the Bad and the Ugly (1966)',  # 97%
        'Harry Potter and the Deathly Hallows: Part 2 (2011)',  # 96%
        'The Silence of the Lambs (1991)',  # 95%
        'Fanny and Alexander (1982)',  # 100%
        'Laura (1944)',  # 100%
        'The Shop Around the Corner (1940)',  # 99%
        'His Girl Friday (1940)',  # 99%
        'All Quiet on the Western Front (1930)',  # 98%
        'Monsters, Inc. (2001)',  # 96%
        'Nights of Cabiria (1957)',  # 100%
        'Pather Panchali (1955)',  # 98%
        'Meet Me in St. Louis (1944)',  # 100%
        'Witness for the Prosecution (1957)',  # 100%
        'Eighth Grade (2018)',  # 99%
        'Rebecca (1940)',  # 98%
        'Stalker (1979)',  # 100%
        'The Terminator (1984)',  # 100%
        'Memento (2000)',  # 94%
        'The Social Network (2010)',  # 96%
        'The Hurt Locker (2008)',  # 96%
        '12 Years a Slave (2013)',  # 95%
        'Catch Me if You Can (2002)',  # 96%
        'Jaws (1975)',  # 97%
        'A Man Escaped (1956)',  # 100%
        'Pan\'s Labyrinth (2006)',  # 95%
        'The Red Shoes (1948)',  # 98%
        'Anatomy of a Murder (1959)',  # 100%
        'Das Boot (1981)',  # 98%
        'Ikiru (1952)',  # 98%
        'Open City (1945)',  # 100%
        'Lady Bird (2017)',  # 99%
        'Hunt for the Wilderpeople (2016)',  # 97%
        'Hell or High Water (2016)',  # 97%
        'Army of Shadows (1969)',  # 97%
        '007: Goldfinger (1964)',  # 99%
        'The Lady Eve (1941)',  # 99%
        'Saving Private Ryan (1998)',  # 94%
        'Ratatouille (2007)',  # 96%
        'Star Trek (2009)',  # 94%
        'The Iron Giant (1999)',  # 96%
        'Monty Python and the Holy Grail Sing-Along (1975)',  # 96%
        'Star Wars: Episode IV - A New Hope (1977)',  # 93%
        'Shadow of a Doubt (1943)',  # 100%
        'WALL-E (2008)',  # 95%
        'Brooklyn (2015)',  # 97%
        'Mr. Smith Goes to Washington (1939)',  # 97%
        'Spider-Man: No Way Home (2021)',  # 93%
        'The Best Years of Our Lives (1946)',  # 98%
        'The Bridge on the River Kwai (1957)',  # 96%
        'Ali: Fear Eats the Soul (1974)',  # 100%
        'Whiplash (2014)',  # 94%
        'The Farewell (2019)',  # 97%
        'Unforgiven (1992)',  # 96%
        'The Adventures of Robin Hood (1938)',  # 100%
        'Pulp Fiction (1994)',  # 92%
        'The King\'s Speech (2010)',  # 94%
        'Leave No Trace (2018)',  # 100%
        'Star Wars: Episode V - The Empire Strikes Back (1980)',  # 95%
        'The Passion of Joan of Arc (1928)',  # 98%
        'Quiz Show (1994)',  # 97%
        'Avengers: Endgame (2019)',  # 94%
        'Ran (1985)',  # 96%
        'Safety Last (1923)',  # 97%
        'Iron Man (2008)',  # 94%
        'Moana (2016)',  # 95%
        'Little Women (2019)',  # 95%
        'Puss in Boots: The Last Wish (2022)',  # 95%
        'Casino Royale (2006)',  # 94%
        'The Handmaiden (2016)',  # 96%
        'La Haine (1995)',  # 96%
        'La Strada (1954)',  # 98%
        'Rashomon (1950)',  # 98%
        'Top Hat (1935)',  # 100%
        'The Artist (2011)',  # 95%
        'The Conformist (1970)',  # 98%
        'One Flew Over the Cuckoo\'s Nest (1975)',  # 93%
        'In the Heat of the Night (1967)',  # 95%
        'Raiders of the Lost Ark (1981)',  # 93%
        'The Peanut Butter Falcon (2019)',  # 95%
        'Paths of Glory (1957)',  # 96%
        'King Kong (1933)',  # 97%
        'Children of Paradise (1945)',  # 98%
        'A Beautiful Day in the Neighborhood (2019)',  # 95%
        'The LEGO Movie (2014)',  # 96%
        'Before Sunset (2004)',  # 94%
        'Soul (2020)',  # 95%
        'Creed (2015)',  # 95%
        'John Wick: Chapter 4 (2023)',  # 94%
        'The Princess Bride (1987)',  # 96%
        'Sunrise (1927)',  # 98%
        'Before Midnight (2013)',  # 98%
        'Lawrence of Arabia (1962)',  # 93%
        'Strangers on a Train (1951)',  # 98%
        'Sling Blade (1996)',  # 97%
        'Kubo and the Two Strings (2016)',  # 97%
        'Sweet Smell of Success (1957)',  # 98%
        'The Thin Man (1934)',  # 98%
        'Once Upon a Time in the West (1968)',  # 96%
        'Eternal Sunshine of the Spotless Mind (2004)',  # 92%
        'Sense and Sensibility (1995)',  # 97%
        'BlacKkKlansman (2018)',  # 96%
        'Lost in Translation (2003)',  # 95%
        'Au Hasard Balthazar (1966)',  # 100%
        'Boyhood (2014)',  # 97%
        'The Grapes of Wrath (1940)',  # 100%
        'Sing Street (2016)',  # 95%
        'A Fistful of Dollars (1964)',  # 98%
        'The Truman Show (1998)',  # 94%
        'Life of Brian (1979)',  # 96%
        '8 1/2 (1963)',  # 97%
        'Marriage Story (2019)',  # 95%
        'Searching for Bobby Fischer (1993)',  # 100%
        'Battleship Potemkin (1925)',  # 100%
        'Sullivan\'s Travels (1941)',  # 100%
        'The Red Circle (1970)',  # 96%
        'The Lost Weekend (1945)',  # 97%
        'Tim Burton\'s The Nightmare Before Christmas (1993)',  # 95%
        'Oppenheimer (2023)',  # 93%
        'The Discreet Charm of the Bourgeoisie (1972)',  # 98%
        'The Lord of the Rings: The Fellowship of the Ring (2001)',  # 92%
        'Ford v Ferrari (2019)',  # 92%
        'My Left Foot (1989)',  # 98%
        'Room (2015)',  # 93%
        'The Lord of the Rings: The Return of the King (2003)',  # 94%
        'A Night at the Opera (1935)',  # 97%
        'Halloween (1978)',  # 96%
        'Air (2023)',  # 93%
        'The Sweet Hereafter (1997)',  # 98%
        'Playtime (1967)',  # 98%
        'True Grit (2010)',  # 95%
        'A Quiet Place (2018)',  # 96%
        'Mudbound (2017)',  # 97%
        'Boyz N the Hood (1991)',  # 96%
        'Brazil (1985)',  # 98%
        'Hidden Figures (2016)',  # 93%
        'Grand Illusion (1937)',  # 97%
        'The Conversation (1974)',  # 93%
        'Fargo (1996)',  # 95%
        'Diabolique (1955)',  # 95%
        'The Apartment (1960)',  # 93%
        'Apollo 13 (1995)',  # 96%
        'Princess Mononoke (1997)',  # 93%
        'Umberto D (1952)',  # 98%
        'Black Panther (2018)',  # 96%
        'Bringing Up Baby (1938)',  # 97%
        'The Sting (1973)',  # 93%
        'Logan (2017)',  # 93%
        'Nightcrawler (2014)',  # 95%
        'The Departed (2006)',  # 91%
        'Juno (2007)',  # 93%
        'Hero (2002)',  # 94%
        'Shaun of the Dead (2004)',  # 92%
        'Stagecoach (1939)',  # 100%
        'Back to the Future (1985)',  # 93%
        'Die Hard (1988)',  # 94%
        'No Country for Old Men (2007)',  # 93%
        'The Lion King (1994)',  # 92%
        'Gravity (2013)',  # 96%
        'The Leopard (1963)',  # 98%
        'Day for Night (1973)',  # 98%
        'Badlands (1973)',  # 97%
        'Touch of Evil (1958)',  # 97%
        'Yojimbo (1961)',  # 96%
        'A Streetcar Named Desire (1951)',  # 97%
        'Breathless (1959)',  # 95%
        'The Manchurian Candidate (1962)',  # 97%
        'The French Connection (1971)',  # 97%
        'The Bourne Ultimatum (2007)',  # 92%
        'My Fair Lady (1964)',  # 94%
        'It\'s a Wonderful Life (1946)',  # 94%
        'Some Like It Hot (1959)',  # 95%
        'The Fugitive (1993)',  # 96%
        'Guardians of the Galaxy (2014)',  # 92%
        'Airplane! (1980)',  # 95%
        'Groundhog Day (1993)',  # 94%
        'This Is Spinal Tap (1984)',  # 96%
        'Beauty and the Beast (1991)',  # 93%
        'The Taking of Pelham One Two Three (1974)',  # 98%
        'City Lights (1931)',  # 95%
        'Kiki\'s Delivery Service (1989)',  # 98%
        'City of God (2002)',  # 91%
        'Rosemary\'s Baby (1968)',  # 97%
        'Call Me by Your Name (2017)',  # 95%
        'Aladdin (1992)',  # 95%
        'The Man With a Movie Camera (1929)',  # 98%
        'The Lady Vanishes (1938)',  # 98%
        'The Umbrellas of Cherbourg (1964)',  # 97%
        'Mission: Impossible Rogue Nation (2015)',  # 94%
        'Three Colors: Blue (1993)',  # 97%
        'Milk (2008)',  # 93%
        'Traffic (2000)',  # 93%
        'Invasion of the Body Snatchers (1956)',  # 97%
        'Thor: Ragnarok (2017)',  # 93%
        'The Odd Couple (1968)',  # 95%
        'Bride of Frankenstein (1935)',  # 98%
        'What\'s Love Got to Do With It (1993)',  # 97%
        'Star Wars: The Force Awakens (2015)',  # 93%
        'Roman Holiday (1953)',  # 96%
        'Amélie (2001)',  # 90%
        'To Be or Not to Be (1942)',  # 96%
        'All the President\'s Men (1976)',  # 94%
        'Throne of Blood (1957)',  # 96%
        'Taxi Driver (1976)',  # 89%
        'The Big Sleep (1946)',  # 96%
        'Marvel\'s the Avengers (2012)',  # 91%
        'Secrets & Lies (1996)',  # 96%
        'Dog Day Afternoon (1975)',  # 96%
        'Being There (1979)',  # 95%
        'Aguirre: The Wrath of God (1972)',  # 96%
        'Arrival (2016)',  # 94%
        'Wings of Desire (1987)',  # 95%
        'Raging Bull (1980)',  # 93%
        'Fruitvale Station (2013)',  # 94%
        'La Dolce Vita (1960)',  # 95%
        'Beauty and the Beast (1946)',  # 96%
        'The Killing (1956)',  # 96%
        'The Rules of the Game (1939)',  # 97%
        'Eyes Without a Face (1960)',  # 97%
        'The Cabinet of Dr. Caligari (1919)',  # 96%
    ]
}

# Initialize session state
if 'user1_matches' not in st.session_state:
    st.session_state.user1_matches = []
if 'user2_matches' not in st.session_state:
    st.session_state.user2_matches = []
if 'current_film' not in st.session_state:
    st.session_state.current_film = random.choice(films['critically acclaimed'])
if 'user1_swipes' not in st.session_state:
    st.session_state.user1_swipes = 0
if 'user2_swipes' not in st.session_state:
    st.session_state.user2_swipes = 0

# Streamlit app layout
st.title("Swipe Left or Right on Films")

# Display the current film
st.write(f"**Current Film:** {st.session_state.current_film}")

# Create boxes for swiping
st.markdown(
    """
    <style>
    .box {
        border: 2px solid #0072B1;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        background-color: #f0f0f0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create buttons for swiping
col1, col2 = st.columns(2)

with col1:
    if st.button("Swipe Left"):
        st.session_state.user1_swipes += 1
        st.session_state.current_film = random.choice(films['critically acclaimed'])
        st.write("You swiped left on:", st.session_state.current_film)

with col2:
    if st.button("Swipe Right"):
        st.session_state.user1_matches.append(st.session_state.current_film)
        st.session_state.user1_swipes += 1
        st.session_state.current_film = random.choice(films['critically acclaimed'])
        st.write("You swiped right on:", st.session_state.current_film)

# Check for matches
if st.session_state.user1_swipes >= 5:
    st.write("You have swiped 5 times!")
    st.write("Your matches:", st.session_state.user1_matches)
    st.stop()

# Display matches
if st.session_state.user1_swipes >= 5:
    st.write("MATCHED!")
    st.write("Discuss your matches:")
    st.write(st.session_state.user1_matches)
