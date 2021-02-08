# Final Project - REVIEWS

##### Door Pranto Bishas  
##### Feedback gegeven door Nick van Santen  

__Overbodige herhaling van contexten__  
Dit is in mijn ogen de belangrijkste feedbackpunt. Contexten worden veel herhaald of bevatten onnodige berekeningen,  
die niet meer van toepassing zijn. Contexten hadden in een aparte functie kunnen staan aangezien de gegevens van de  
navigatiebalk en footer er altijd in staan. Context herhalingen konden verkomen worden als er meer gewerkt werd met  
if en else statements.

__Gebruik van globale variabelen__  
Voor veiligheidsredenen was het verstandig geweest om het wachtwoord van mijn settings.py (EMAIL_HOST_PASSWORD)  
als globale variabele te vermelden. Deze e-mail is aangemaakt voor gebruikt van django en is dus niet mijn  
persoonlijke mail, maar de berichten en gegevens van de gebruikers zijn wel weer te zien in de gekregen mails.  
Ook zijn typefouten te voorkomen door meer gebruik van globale variabelen.

__CATEGORIES keuzemenu in skager.models als class maken__  
Voor de model Product is een keuzemenu gemaakt voor de categorie van het product. Voor de gebruikersvriendelijkheid  
is het dan verstandiger om van de keuzemenu CATEGORIES een class te maken, waarbij de admin gemakkelijk categoriën  
kan toevoegen en verwijderen.  

__De models ToysList en SchoolList in skager.models zijn overbodig__  
Deze modellen bevatten de categoriën die weergegeven worden in de dropdown-menu van de navbar. Deze categoriën  
konden ook verkregen worden van de CATEGORIES keuzemenu of filteren op de doelcategoriën.

__Gebruik van docstrings__  
Voor de standaard layout van comments is het gebruikelijk om een docstring te vermelden *onder* de functies.  
Ze staan er nu boven als *hashed* comments.



