from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'

class About_ICCIT(TemplateView):
    template_name = 'about_iccit.html'

class About_NSU(TemplateView):
    template_name = 'about_nsu.html'

class Accepted_Papers(TemplateView):
    template_name = 'accepted_papers.html'

class Call_For_Paper(TemplateView):
    template_name = 'call_for_paper.html'

class Contact(TemplateView):
    template_name = 'contact.html'

class Important_Dates(TemplateView):
    template_name = 'important_dates.html'

class Organizing_Committee(TemplateView):
    template_name = 'organizing_committee.html'

class Paper_Submission_Guidelines(TemplateView):
    template_name = 'paper_submission_guidelines.html'

class Patrons(TemplateView):
    template_name = 'patrons.html'

class Plagiarism(TemplateView):
    template_name = 'plagiarism.html'

class Registration(TemplateView):
    template_name = 'registration.html'

class Technical_Committee(TemplateView):
    template_name = 'technical_committee.html'

class Publications(TemplateView):
    template_name = 'publications.html'

class Speakers(TemplateView):
    template_name = 'speakers.html'

class Research_Integrity_Committee(TemplateView):
    template_name = 'research_integrity_committee.html'

class BestPaperAward(TemplateView):
    template_name = 'best_paper_award.html'

class Camera_Ready_Paper_Submission_Guidelines(TemplateView):
    template_name = 'camera_ready_paper_submission_guidelines.html'

class Workshop_1(TemplateView):
    template_name = 'workshop_1.html'

class Workshop_2(TemplateView):
    template_name = 'workshop_2.html'

class Tutorial_1(TemplateView):
    template_name = 'tutorial_1.html'

class Tutorial_2(TemplateView):
    template_name = 'tutorial_2.html'

# Speakers
class Prof_Jie_Wu(TemplateView):
    template_name = 'speakers/prof-jie-wu.html'

class Prof_Ayman_Alfalou(TemplateView):
    template_name = 'speakers/prof-ayman-alfalou.html'

class Vijayan_K_Asari(TemplateView):
    template_name = 'speakers/vijayan-k-asari.html'

class Prof_Mohsen_Guizani(TemplateView):
    template_name = 'speakers/prof-mohsen-guizani.html'

class Prof_Muhammad_H_Rashid(TemplateView):
    template_name = 'speakers/prof-m-h-rashid.html'

class Anjani_Phuyal(TemplateView):
    template_name = 'speakers/anjani_phuyal.html'

class Dr_Ishtiaque_Ahmed(TemplateView):
    template_name = 'speakers/dr-ishtiaque-ahmed.html'

class Dr_Sheikh_Iqbal_Ahamed(TemplateView):
    template_name = 'speakers/dr-sheikh-iqbal-ahamed.html'

class Prof_Swagatam_Das(TemplateView):
    template_name = 'speakers/prof-swagatam-das.html'

class Mohammed_Atiquzzaman(TemplateView):
    template_name = 'speakers/mohammed-atiquzzaman.html'

class Dr_Thomas_Lu(TemplateView):
    template_name = 'speakers/dr-thomas-lu.html'

class Sponsor(TemplateView):
    template_name = 'sponsor.html'


class Robots(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
