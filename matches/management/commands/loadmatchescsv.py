from django.core.management.base import BaseCommand, CommandError

from matches.models import Match

from datetime import datetime

class Command(BaseCommand):
    help = 'Upload matches data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path')

    def handle(self, *args, **options):
        file_path = options['csv_file_path']
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines[1:]:
                split_line = line.split(",")
                if len(split_line) > 1:
                    dl_applied = False
                    if split_line[9]:
                        dl_applied = True
                    data = {
                        "season": int(split_line[1].split("-")[1]),
                        "city": split_line[2],
                        "date": datetime.strptime(split_line[3],'%d-%m-%Y'),
                        "team1": split_line[4],
                        "team2": split_line[5],
                        "toss_winner": split_line[6],
                        "toss_decision": split_line[7],
                        "result": split_line[8],
                        "dl_applied": dl_applied,
                        "winner": split_line[10],
                        "win_by_runs": split_line[11],
                        "win_by_wickets": split_line[12],
                        "player_of_match": split_line[13],
                        "venue": split_line[14],
                        "umpire1": split_line[15],
                        "umpire2": split_line[16].strip(),
                    }
                    match = Match.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('Successfully uploaded data'))