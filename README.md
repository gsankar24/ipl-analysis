# ipl-analysis
Ipl seasons analysis with HighChart 

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* python3
* python3-venv

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/gsankar24/ipl-analysis.git
   ```
2. Change directry to ipl-analysis folder
    ```sh
   cd ipl-analysis
   ```
3. Create virtual environment
   ```sh
   python3 -m venv venv
   ```
4. Activate environment
   ```sh
   source venv/bin/activate
   ```
5. Install requirements packages
   ```sh
   pip install -r requirements.txt
   ```
   
## Run

1. Migrate database 
   ```sh
   python manage.py migrate
   ```
2. Load ipl data 
   ```sh
   python manage.py loadmatchescsv 'data/matches.csv'
   ```
3. Run server
    ```sh
   python manage.py runserver
   ```
Open url: http://localhost:8000 in browser.
