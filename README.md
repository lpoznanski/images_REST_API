# images_REST_API
This is a simple DRF application that allows users to upload images and displays images according to the user's tier.

There are three builtin account tiers: Basic, Premium and Enterprise. Depending on the tier, users get links to thumbnails or the originally added image.

#### How to add new tiers?
Admin can add new tiers in the Django admin panel.
1. Create a new group.
2. Create new group details. You can now select if the new tier should have acces to the original uploaded image.
3. Add existing thumbnails properties to group details or create new ones.

### How to run this?
1. Install Docker Compose  if you don't already have it.
2. Clone this repository
3. Run all containers with `docker-compose up`
