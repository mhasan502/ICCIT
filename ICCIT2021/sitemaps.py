from django.contrib import sitemaps
from django.urls import reverse


class Sitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'about_iccit', 'about_nsu', 'accepted_papers','call_for_paper', 'contact',
            'important_dates', 'organizing_committee', 'paper_submission_guidelines',
            'patrons', 'plagiarism', 'registration', 'technical_committee', 'publications',
            'speakers', 'research_integrity_committee', 'best_paper_award', 'sponsor',
            'camera_ready_paper_submission_guidelines', 'workshop_1', 'workshop_2',
            'tutorial_1', 'tutorial_2',
            'anjani-phuyal', 'dr-ishtiaque_ahmed', 'dr-sheikh-iqbal-ahamed',
            'dr-thomas-lu', 'mohammed-atiquzzaman', 'prof-ayman-alfalou', 'prof-jie-wu',
            'prof-muhammad-h-rashid', 'prof-mohsen-guizani', 'prof-swagatam-das',
            'vijayan-k-asari'
        ]

    def location(self, item):
        return reverse(item)