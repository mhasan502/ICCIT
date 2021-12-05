from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about_iccit.html', About_ICCIT.as_view(), name='about_iccit'),
    path('about_nsu.html', About_NSU.as_view(), name='about_nsu'),
    path('accepted_papers.html', Accepted_Papers.as_view(), name='accepted_papers'),
    path('call_for_paper.html', Call_For_Paper.as_view(), name='call_for_paper'),
    path('contact.html', Contact.as_view(), name='contact'),
    path('important_dates.html', Important_Dates.as_view(), name='important_dates'),
    path('organizing_committee.html', Organizing_Committee.as_view(), name='organizing_committee'),
    path('paper_submission_guidelines.html', Paper_Submission_Guidelines.as_view(), name='paper_submission_guidelines'),
    path('patrons.html', Patrons.as_view(), name='patrons'),
    path('plagiarism.html', Plagiarism.as_view(), name='plagiarism'),
    path('registration.html', Registration.as_view(), name='registration'),
    path('technical_committee.html', Technical_Committee.as_view(), name='technical_committee'),
    path('publications.html', Publications.as_view(), name='publications'),
    path('speakers.html', Speakers.as_view(), name='speakers'),
    path('research_integrity_committee.html', Research_Integrity_Committee.as_view(), name='research_integrity_committee'),
    path('best_paper_award.html', BestPaperAward.as_view(), name='best_paper_award'),
    path('camera_ready_paper_submission_guidelines.html', Camera_Ready_Paper_Submission_Guidelines.as_view(), name='camera_ready_paper_submission_guidelines'),
    path('workshop_1.html', Workshop_1.as_view(), name='workshop_1'),
    path('workshop_2.html', Workshop_2.as_view(), name='workshop_2'),
    path('tutorial_1.html', Tutorial_1.as_view(), name='tutorial_1'),
    path('tutorial_2.html', Tutorial_2.as_view(), name='tutorial_2'),

    # Speakers
    path('anjani-phuyal.html', Anjani_Phuyal.as_view(), name='anjani-phuyal'),
    path('dr-ishtiaque-ahmed.html', Dr_Ishtiaque_Ahmed.as_view(), name='dr-ishtiaque_ahmed'),
    path('dr-sheikh-iqbal-ahamed.html', Dr_Sheikh_Iqbal_Ahamed.as_view(), name='dr-sheikh-iqbal-ahamed'),
    path('dr-thomas-lu.html', Dr_Thomas_Lu.as_view(), name='dr-thomas-lu'),
    path('mohammed-atiquzzaman.html', Mohammed_Atiquzzaman.as_view(), name='mohammed-atiquzzaman'),
    path('prof-ayman-alfalou.html', Prof_Ayman_Alfalou.as_view(), name='prof-ayman-alfalou'),
    path('prof-jie-wu.html', Prof_Jie_Wu.as_view(), name='prof-jie-wu'),
    path('prof-muhammad-h-rashid.html', Prof_Muhammad_H_Rashid.as_view(), name='prof-muhammad-h-rashid'),
    path('prof-mohsen-guizani.html', Prof_Mohsen_Guizani.as_view(), name='prof-mohsen-guizani'),
    path('prof-swagatam-das.html', Prof_Swagatam_Das.as_view(), name='prof-swagatam-das'),
    path('vijayan-k-asari.html', Vijayan_K_Asari.as_view(), name='vijayan-k-asari'),

    path('robots.txt', Robots.as_view(), name='robots'),
]
