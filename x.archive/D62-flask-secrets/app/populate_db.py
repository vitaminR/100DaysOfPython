import sys
import os

# Ensure the script can find the app module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app, db
from app.models import Cafe

app = create_app()

with app.app_context():
    cafe1 = Cafe(
        name="Cafe 1",
        map_url="http://example.com",
        img_url="http://example.com/img1.jpg",
        location="Location 1",
        seats="50",
        has_toilet=True,
        has_wifi=True,
        has_sockets=True,
        can_take_calls=True,
        coffee_price="$2.5",
    )
    cafe2 = Cafe(
        name="Cafe 2",
        map_url="http://example.com",
        img_url="http://example.com/img2.jpg",
        location="Location 2",
        seats="30",
        has_toilet=True,
        has_wifi=True,
        has_sockets=False,
        can_take_calls=False,
        coffee_price="$3.0",
    )
    db.session.add(cafe1)
    db.session.add(cafe2)
    db.session.commit()

print("Database has been populated successfully.")
