# DJ Mixes Project

This is a web application for DJs and music enthusiasts. It allows DJs to manage their mixes and profiles, and it allows users to browse mixes by different DJs and genres.

## Features

- DJs can create, update, and delete their profiles.
- DJs can create, update, and delete their mixes.
- Mixes can be tagged with multiple tags.
- Users can browse mixes by DJ, genre, or tag.

## Tech Stack

- Python
- Django
- PostgreSQL
- Docker

## Getting Started

1. Clone this repository.
2. Install Docker and Docker Compose.
3. Run `docker-compose build` to build the Docker images.
4. Run `docker-compose up` to start the application.

## API Endpoints

The application provides the following API endpoints:

- `/djs`: GET a list of all DJs, POST a new DJ
- `/djs/<dj_id>`: GET, PUT, DELETE a specific DJ
- `/djs/<dj_id>/profile`: GET, PUT, DELETE the profile of a specific DJ
- `/djs/<dj_id>/mixes`: GET a list of all mixes by a specific DJ, POST a new mix
- `/mixes/<mix_id>`: GET, PUT, DELETE a specific mix
- `/mixes/<mix_id>/tags`: GET a list of all tags for a specific mix, POST a new tag
- `/tags/<tag_id>`: GET, PUT, DELETE a specific tag

## Database Schema

The application uses the following database tables:

- `djs`: Stores information about DJs. Columns: `dj_id` (Primary Key), `name`, `email`, `phone`
- `profiles`: Stores profiles for DJs. Columns: `profile_id` (Primary Key), `bio`, `location`, `dj_id` (Foreign Key referencing `djs`)
- `mixes`: Stores information about mixes. Columns: `mix_id` (Primary Key), `title`, `genre`, `duration`, `release_date`, `dj_id` (Foreign Key referencing `djs`)
- `tags`: Stores information about tags. Columns: `tag_id` (Primary Key), `tag_name`
- `mix_tags`: Stores the many-to-many relationship between mixes and tags. Columns: `mix_id` (Foreign Key referencing `mixes`), `tag_id` (Foreign Key referencing `tags`)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.