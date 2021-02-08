# Final Project - PROCESS

##### www.skagermultishop.nl
##### By Pranto Bishas

__04/12/2019__  
Ik moest even opzoeken hoe een django-project kon worden aangemaakt, omdat er bij *Pizza* al een applicatie voor   
ons was aangemaakt. Django's eigen registratie formulier is Engels, terwijl ik een Nederlandse site wil maken.  
Ik zal achteraf een eigen Nederlandse registratie formulier maken.  

__05/12/2019__  
Het ordenen van alle producten in de winkel wordt lastig om in de navigatiebalk te verwerken. Ik heb nu de  
hoofdklasse staan in de balk en categorieën als *dropdown* eronder weergegeven.  

__06/12/2019__  
Het werken met twee aparte apps, moest anders worden weergegeven in de hoofdapp *Web_app*. De pagina moet  
toegankelijk zijn voor bezoekers met of zonder account. Het pad zonder input ("") moet de app *skager*  
bevatten met alle componenten van de doelsite. De *paths* voor inloggen, uitloggen en registreren heb ik  
hiervoor in de hoofdapp urls verwerkt. Het duurde even voordat ik de *foreign exchange api* kon laten werken,  
en de mogelijke buggs uit de pagina eruit geprobeerd te halen.

__09/12/2019__  
Het tellen van alle objecten van dezelfde product in de winkelwagen, was lastiger dan ik dacht. Ik heb een manier  
gevonden om een *dictionary* te maken van de naam van het product met het aantal in de winkelwagen. De site is  
in het Nederlands, maar de code staat nu grootendeels in het Engels, aangezien veel codetaal in het Engels is.

__10/12/2019__  
Ik vind het maar lastig om het aantal producten gemakkelijk weer te geven in de winkelwagen met de opgetelde prijs  
van het aantal producten van een soort. Ik merk dat ik voor sommige defenities vaker een context heb vermeld, maar  
dat heb ik express staan aangezien de context veranderd na een bepaalde actie of zoekresultaat.

__11/12/2019__  
Ik begin me te beseffen dat mijn modellen niet handig zijn, er worden teveel objecten aangemaakt als een product  
wordt toegevoegd. Ook moeten er achteraf berekeningen worden gedaan over het aantal producten van dezelfde soort  
en de uiteindelijke prijs. Heb momenteel een veel handiger model ontwikkeld, waarbij het aantal en totale prijs  
staat weergegeven. Deze waarden worden veranderd wanneer er een product van dezelfde soort wordt toegevoegd of  
verwijderd, hierdoor staat er maar 1 object per categorie weergegeven in de winkelwagen.

__12/12/2019__  
Ik ben langsgegaan bij de winkel zelf om informatie en foto's te regelen voor de site. De opdracht en mijn instelling  
is totaal niet om kwantitatief alle producten op de site te zetten, maar de kwaliteit achter de code. De admin moet  
vrij gemakkelijk een product via het admin-menu van django kunnen toevoegen, daarvoor heb ik ook een optie-menu gemaakt  
voor de categorie van de producten (typefouten kunnen te vaak voorkomen en dit is een stuk handiger). Verder heb ik  
mijn code nog eens kritisch bekeken en zag dat ik stukjes code beter in een aparte definitie kan verwerken en de benodigde  
waarden kan *returnen*. Ook heb ik stukjes die voornamelijk *gehardcode* waren kunnen vervangen door enkele regels.  
De functionaliteit komt nu grootendeels naar voren, echter wil ik de omgekeerde kant van het rekenen met wisselkoersen  
en een veel betere layout nog gaan toepassen.  

__13/12/2019__  
Ben erachter gekomen dat de bevestigingsmail een bug heeft, maar de bestelling wordt soms wel en soms niet weergegeven  
in de mail, ookal wordt er dezelfde code gebruikt. Deze bug niet kunnen achterhalen, maar hij blijkt het nog te doen.  
Ik heb contexten geminimaliseerd door objecten toe te voegen of te veranderen, omdat het *dictionaries* zijn.  
Ik wil nog verder werken aan de layout, het soort van omkeren van het berekenen met wisselkoersen en een searchbar. Dit  
is wellicht niet meer haalbaar, maar ik zal proberen zo ver mogelijk te komen.

__15/12/2019__  
Er zijn nog een paar punten waar ik nog niet tevreden mee ben. Het eerste punt is, is dat mijn inlog en registratie scherm  
in het Engels staan. Dit komt doordat de django-registrationform in het Engels is. Ik moet dus de keuze maken om een eigen  
registratie forum te maken met een minder goede validatie methode, omdat alle htmls dan in het Nederlands staan. Of ik houd  
zowel het inlog- als registratiescherm in het Engels en behoud de prima layout en handige django-form. Een ander punt is het  
weergegeven van de productfoto's. Elke product heeft zijn eigen vorm en grootte, maar ik wil alle producten als dezelfde  
soort kaart kunnen weergegeven. Hierbij heb ik de keuze gemaakt om alle foto's op dezelfde wijze te fotograferen, waarbij  
langwerpige objecten minder mooi zijn weergegeven.  

__16/12/2019__  
Heb toch de django-registratie form opgegeven for een Nederlandse registratie- en login-pagina. Een error.html toegevoegd als  
men een niet geldige url zoekt. De code door een ander proberen te laten kraken, maar tot nu toe nog geen buggs kunnen vinden.  
De README.md is nog steeds snel in elkaar geflansd, aangezien ik door speciale redenen in tijdnood kwam. Ik wilde deze nog  
aanpassen, maar ik legde mijn prioriteiten op de site zelf. Ik heb nu de afbeeldingen die gebruikt zijn in voor de site in  
static-folders en een media-folder (de productafbeeldingen) staan.