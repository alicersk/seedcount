import streamlit as st
import pandas as pd
import random
import altair as alt

#To run, paste into terminal: streamlit run streamlitapp.py

"""
# Seed Count
Attempt to make the streamlit app to test some code
"""

print("Here is the list of seeds:")
DATA = pd.read_csv("SEEDS.csv",
                   header=0,
                   index_col=False,
                   names=['seeds_per_lb', 'seeds_per_oz', 'species', 'nan', 'altname', 
                          'common_name', 'ecotypes', 'germ_protocol', 'forb', 'fall', 'germ_rate',
                          'a', 'm', 'j', 'j2', 'a2', 's', 'o'])

SEEDLIST_raw = DATA[["species", "common_name", "seeds_per_lb", "germ_rate"]]
SEEDLIST = SEEDLIST_raw.drop_duplicates(subset=['species'])
SEEDLIST
SPLIST = SEEDLIST["species"].tolist()

#create empty list to store choices
usrchoices = []

#make the choices using checkboxes
	#this code is copy-pasted from "checkboxes.txt" and was generated with 'makeboxes.py'
	#I think there is a much more elegant way to do this, but I did want to see
	#if you could use checkboxes instead of the drop-down menu, which is not my
	#personal preferred way of making choices
achilleamillefolium = st.checkbox('Achillea millefolium')
if achilleamillefolium:
	usrchoices.append('Achillea millefolium')
acorusamericanus = st.checkbox('Acorus americanus')
if acorusamericanus:
	usrchoices.append('Acorus americanus')
agastachefoeniculum = st.checkbox('Agastache foeniculum')
if agastachefoeniculum:
	usrchoices.append('Agastache foeniculum')
agrimoniaparviflora = st.checkbox('Agrimonia parviflora')
if agrimoniaparviflora:
	usrchoices.append('Agrimonia parviflora')
agrostisalba = st.checkbox('Agrostis alba')
if agrostisalba:
	usrchoices.append('Agrostis alba')
agrostishyemalis = st.checkbox('Agrostis hyemalis')
if agrostishyemalis:
	usrchoices.append('Agrostis hyemalis')
agrostisperennans = st.checkbox('Agrostis perennans')
if agrostisperennans:
	usrchoices.append('Agrostis perennans')
agrostisscabra = st.checkbox('Agrostis scabra')
if agrostisscabra:
	usrchoices.append('Agrostis scabra')
agrostisstolonifera = st.checkbox('Agrostis stolonifera')
if agrostisstolonifera:
	usrchoices.append('Agrostis stolonifera')
agrostistenuis = st.checkbox('Agrostis tenuis')
if agrostistenuis:
	usrchoices.append('Agrostis tenuis')
alismasubcordatum = st.checkbox('Alisma subcordatum')
if alismasubcordatum:
	usrchoices.append('Alisma subcordatum')
alliumcernuum = st.checkbox('Allium cernuum')
if alliumcernuum:
	usrchoices.append('Allium cernuum')
alopecurusarundianceus = st.checkbox('Alopecurus arundianceus')
if alopecurusarundianceus:
	usrchoices.append('Alopecurus arundianceus')
ammimajus = st.checkbox('Ammi majus')
if ammimajus:
	usrchoices.append('Ammi majus')
amorphacanescens = st.checkbox('Amorpha canescens')
if amorphacanescens:
	usrchoices.append('Amorpha canescens')
amorphafruticosa = st.checkbox('Amorpha fruticosa')
if amorphafruticosa:
	usrchoices.append('Amorpha fruticosa')
amorphaherbacea = st.checkbox('Amorpha herbacea')
if amorphaherbacea:
	usrchoices.append('Amorpha herbacea')
amsoniaciliata = st.checkbox('Amsonia ciliata')
if amsoniaciliata:
	usrchoices.append('Amsonia ciliata')
andropogongerardii = st.checkbox('Andropogon gerardii')
if andropogongerardii:
	usrchoices.append('Andropogon gerardii')
andropogonglomeratus = st.checkbox('Andropogon glomeratus ')
if andropogonglomeratus:
	usrchoices.append('Andropogon glomeratus ')
andropogonglomeratusvarglaucopsis = st.checkbox('Andropogon glomeratus var. glaucopsis')
if andropogonglomeratusvarglaucopsis:
	usrchoices.append('Andropogon glomeratus var. glaucopsis')
andropogonternarius = st.checkbox('Andropogon ternarius')
if andropogonternarius:
	usrchoices.append('Andropogon ternarius')
andropogonvirginicus = st.checkbox('Andropogon virginicus')
if andropogonvirginicus:
	usrchoices.append('Andropogon virginicus')
anemonecanadensis = st.checkbox('Anemone canadensis')
if anemonecanadensis:
	usrchoices.append('Anemone canadensis')
anemonevirginiana = st.checkbox('Anemone virginiana')
if anemonevirginiana:
	usrchoices.append('Anemone virginiana')
apocynumcannabinum = st.checkbox('Apocynum cannabinum')
if apocynumcannabinum:
	usrchoices.append('Apocynum cannabinum')
aquilegiacanadensis = st.checkbox('Aquilegia canadensis')
if aquilegiacanadensis:
	usrchoices.append('Aquilegia canadensis')
asclepiasincarnata = st.checkbox('Asclepias incarnata')
if asclepiasincarnata:
	usrchoices.append('Asclepias incarnata')
asclepiassyriaca = st.checkbox('Asclepias syriaca')
if asclepiassyriaca:
	usrchoices.append('Asclepias syriaca')
asclepiastuberosa = st.checkbox('Asclepias tuberosa')
if asclepiastuberosa:
	usrchoices.append('Asclepias tuberosa')
asterdivaricatus = st.checkbox('Aster divaricatus')
if asterdivaricatus:
	usrchoices.append('Aster divaricatus')
asterlaevis = st.checkbox('Aster laevis')
if asterlaevis:
	usrchoices.append('Aster laevis')
asterlowrieanus = st.checkbox('Aster lowrieanus')
if asterlowrieanus:
	usrchoices.append('Aster lowrieanus')
astermacrophyllus = st.checkbox('Aster macrophyllus')
if astermacrophyllus:
	usrchoices.append('Aster macrophyllus')
asternovaeangliae = st.checkbox('Aster novae-angliae')
if asternovaeangliae:
	usrchoices.append('Aster novae-angliae')
asternovibelgii = st.checkbox('Aster novi-belgii')
if asternovibelgii:
	usrchoices.append('Aster novi-belgii')
asteroblongifolius = st.checkbox('Aster oblongifolius')
if asteroblongifolius:
	usrchoices.append('Aster oblongifolius')
asterpatens = st.checkbox('Aster patens')
if asterpatens:
	usrchoices.append('Aster patens')
asterpilosus = st.checkbox('Aster pilosus')
if asterpilosus:
	usrchoices.append('Aster pilosus')
asterprenanthoides = st.checkbox('Aster prenanthoides')
if asterprenanthoides:
	usrchoices.append('Aster prenanthoides')
asterpuniceus = st.checkbox('Aster puniceus')
if asterpuniceus:
	usrchoices.append('Aster puniceus')
astersagittifolius = st.checkbox('Aster sagittifolius')
if astersagittifolius:
	usrchoices.append('Aster sagittifolius')
asterspectabilis = st.checkbox('Aster spectabilis')
if asterspectabilis:
	usrchoices.append('Aster spectabilis')
asterumbellatus = st.checkbox('Aster umbellatus')
if asterumbellatus:
	usrchoices.append('Aster umbellatus')
baptisiaalba = st.checkbox('Baptisia alba')
if baptisiaalba:
	usrchoices.append('Baptisia alba')
baptisiaalbescens = st.checkbox('Baptisia albescens')
if baptisiaalbescens:
	usrchoices.append('Baptisia albescens')
baptisiaaustralis = st.checkbox('Baptisia australis')
if baptisiaaustralis:
	usrchoices.append('Baptisia australis')
baptisiacinerea = st.checkbox('Baptisia cinerea')
if baptisiacinerea:
	usrchoices.append('Baptisia cinerea')
baptisiapendula = st.checkbox('Baptisia pendula')
if baptisiapendula:
	usrchoices.append('Baptisia pendula')
baptisiaperfoliata = st.checkbox('Baptisia perfoliata')
if baptisiaperfoliata:
	usrchoices.append('Baptisia perfoliata')
baptisiatinctoria = st.checkbox('Baptisia tinctoria')
if baptisiatinctoria:
	usrchoices.append('Baptisia tinctoria')
bidensaristosa = st.checkbox('Bidens aristosa')
if bidensaristosa:
	usrchoices.append('Bidens aristosa')
bidenscernua = st.checkbox('Bidens cernua')
if bidenscernua:
	usrchoices.append('Bidens cernua')
bidensfrondosa = st.checkbox('Bidens frondosa')
if bidensfrondosa:
	usrchoices.append('Bidens frondosa')
blephiliaciliata = st.checkbox('Blephilia ciliata')
if blephiliaciliata:
	usrchoices.append('Blephilia ciliata')
boltoniaasteroides = st.checkbox('Boltonia asteroides')
if boltoniaasteroides:
	usrchoices.append('Boltonia asteroides')
boutelouacurtipendula = st.checkbox('Bouteloua curtipendula')
if boutelouacurtipendula:
	usrchoices.append('Bouteloua curtipendula')
boutelouagracilis = st.checkbox('Bouteloua gracilis')
if boutelouagracilis:
	usrchoices.append('Bouteloua gracilis')
bromusinermis = st.checkbox('Bromus inermis')
if bromusinermis:
	usrchoices.append('Bromus inermis')
buchloedactyloides = st.checkbox('Buchloe dactyloides')
if buchloedactyloides:
	usrchoices.append('Buchloe dactyloides')
calamagrostiscanadensis = st.checkbox('Calamagrostis canadensis')
if calamagrostiscanadensis:
	usrchoices.append('Calamagrostis canadensis')
calendulaofficinalis = st.checkbox('Calendula officinalis')
if calendulaofficinalis:
	usrchoices.append('Calendula officinalis')
carexalata = st.checkbox('Carex alata')
if carexalata:
	usrchoices.append('Carex alata')
carexalbolutescens = st.checkbox('Carex albolutescens')
if carexalbolutescens:
	usrchoices.append('Carex albolutescens')
carexcomosa = st.checkbox('Carex comosa')
if carexcomosa:
	usrchoices.append('Carex comosa')
carexcrinita = st.checkbox('Carex crinita')
if carexcrinita:
	usrchoices.append('Carex crinita')
carexfolliculata = st.checkbox('Carex folliculata')
if carexfolliculata:
	usrchoices.append('Carex folliculata')
carexfrankii = st.checkbox('Carex frankii')
if carexfrankii:
	usrchoices.append('Carex frankii')
carexglaucescens = st.checkbox('Carex glaucescens')
if carexglaucescens:
	usrchoices.append('Carex glaucescens')
carexgranularisvarhaleana = st.checkbox('Carex granularis var. haleana')
if carexgranularisvarhaleana:
	usrchoices.append('Carex granularis var. haleana')
carexgrayi = st.checkbox('Carex grayi')
if carexgrayi:
	usrchoices.append('Carex grayi')
carexgynandra = st.checkbox('Carex gynandra')
if carexgynandra:
	usrchoices.append('Carex gynandra')
carexintumescens = st.checkbox('Carex intumescens')
if carexintumescens:
	usrchoices.append('Carex intumescens')
carexlacustris = st.checkbox('Carex lacustris')
if carexlacustris:
	usrchoices.append('Carex lacustris')
carexlupulina = st.checkbox('Carex lupulina')
if carexlupulina:
	usrchoices.append('Carex lupulina')
carexlurida = st.checkbox('Carex lurida')
if carexlurida:
	usrchoices.append('Carex lurida')
carexscoparia = st.checkbox('Carex scoparia')
if carexscoparia:
	usrchoices.append('Carex scoparia')
carexsquarrosa = st.checkbox('Carex squarrosa')
if carexsquarrosa:
	usrchoices.append('Carex squarrosa')
carexstipata = st.checkbox('Carex stipata')
if carexstipata:
	usrchoices.append('Carex stipata')
carexstricta = st.checkbox('Carex stricta')
if carexstricta:
	usrchoices.append('Carex stricta')
carexvulpinoidea = st.checkbox('Carex vulpinoidea')
if carexvulpinoidea:
	usrchoices.append('Carex vulpinoidea')
centaureacyanus = st.checkbox('Centaurea cyanus')
if centaureacyanus:
	usrchoices.append('Centaurea cyanus')
chamaecristafasciculata = st.checkbox('Chamaecrista fasciculata')
if chamaecristafasciculata:
	usrchoices.append('Chamaecrista fasciculata')
chamaecristanictitans = st.checkbox('Chamaecrista nictitans')
if chamaecristanictitans:
	usrchoices.append('Chamaecrista nictitans')
chasmanthiumlatifolium = st.checkbox('Chasmanthium latifolium')
if chasmanthiumlatifolium:
	usrchoices.append('Chasmanthium latifolium')
chasmanthiumlaxum = st.checkbox('Chasmanthium laxum')
if chasmanthiumlaxum:
	usrchoices.append('Chasmanthium laxum')
cheiranthusallionii = st.checkbox('Cheiranthus allionii')
if cheiranthusallionii:
	usrchoices.append('Cheiranthus allionii')
cheloneglabra = st.checkbox('Chelone glabra')
if cheloneglabra:
	usrchoices.append('Chelone glabra')
chrysanthemumcarinatum = st.checkbox('Chrysanthemum carinatum')
if chrysanthemumcarinatum:
	usrchoices.append('Chrysanthemum carinatum')
chrysanthemumleucanthemum = st.checkbox('Chrysanthemum leucanthemum')
if chrysanthemumleucanthemum:
	usrchoices.append('Chrysanthemum leucanthemum')
chrysanthemummaximum = st.checkbox('Chrysanthemum maximum')
if chrysanthemummaximum:
	usrchoices.append('Chrysanthemum maximum')
cichoriumintybus = st.checkbox('Cichorium intybus')
if cichoriumintybus:
	usrchoices.append('Cichorium intybus')
cimicifugaracemosa = st.checkbox('Cimicifuga racemosa')
if cimicifugaracemosa:
	usrchoices.append('Cimicifuga racemosa')
cinnaarundinacea = st.checkbox('Cinna arundinacea')
if cinnaarundinacea:
	usrchoices.append('Cinna arundinacea')
clarkiaelegans = st.checkbox('Clarkia elegans')
if clarkiaelegans:
	usrchoices.append('Clarkia elegans')
coreopsisbasalis = st.checkbox('Coreopsis basalis')
if coreopsisbasalis:
	usrchoices.append('Coreopsis basalis')
coreopsisgrandiflora = st.checkbox('Coreopsis grandiflora')
if coreopsisgrandiflora:
	usrchoices.append('Coreopsis grandiflora')
coreopsislanceolata = st.checkbox('Coreopsis lanceolata')
if coreopsislanceolata:
	usrchoices.append('Coreopsis lanceolata')
coreopsisleavenworthii = st.checkbox('Coreopsis leavenworthii')
if coreopsisleavenworthii:
	usrchoices.append('Coreopsis leavenworthii')
coreopsismajor = st.checkbox('Coreopsis major')
if coreopsismajor:
	usrchoices.append('Coreopsis major')
coreopsistinctoria = st.checkbox('Coreopsis tinctoria')
if coreopsistinctoria:
	usrchoices.append('Coreopsis tinctoria')
coreopsistripteris = st.checkbox('Coreopsis tripteris')
if coreopsistripteris:
	usrchoices.append('Coreopsis tripteris')
coreopsisverticillata = st.checkbox('Coreopsis verticillata')
if coreopsisverticillata:
	usrchoices.append('Coreopsis verticillata')
cosmosbipinnatus = st.checkbox('Cosmos bipinnatus')
if cosmosbipinnatus:
	usrchoices.append('Cosmos bipinnatus')
cosmossulphureus = st.checkbox('Cosmos sulphureus')
if cosmossulphureus:
	usrchoices.append('Cosmos sulphureus')
crotoncapitatus = st.checkbox('Croton capitatus')
if crotoncapitatus:
	usrchoices.append('Croton capitatus')
dactylisglomerata = st.checkbox('Dactylis glomerata')
if dactylisglomerata:
	usrchoices.append('Dactylis glomerata')
daleacandida = st.checkbox('Dalea candida')
if daleacandida:
	usrchoices.append('Dalea candida')
daleapurpurea = st.checkbox('Dalea purpurea')
if daleapurpurea:
	usrchoices.append('Dalea purpurea')
daucuscarota = st.checkbox('Daucus carota')
if daucuscarota:
	usrchoices.append('Daucus carota')
delphiniumajacis = st.checkbox('Delphinium ajacis')
if delphiniumajacis:
	usrchoices.append('Delphinium ajacis')
desmanthusillinoensis = st.checkbox('Desmanthus illinoensis')
if desmanthusillinoensis:
	usrchoices.append('Desmanthus illinoensis')
desmodiumcanadense = st.checkbox('Desmodium canadense')
if desmodiumcanadense:
	usrchoices.append('Desmodium canadense')
desmodiumglabellum = st.checkbox('Desmodium glabellum')
if desmodiumglabellum:
	usrchoices.append('Desmodium glabellum')
desmodiumpaniculatum = st.checkbox('Desmodium paniculatum')
if desmodiumpaniculatum:
	usrchoices.append('Desmodium paniculatum')
desmodiumtortuosum = st.checkbox('Desmodium tortuosum')
if desmodiumtortuosum:
	usrchoices.append('Desmodium tortuosum')
dianthusbarbatus = st.checkbox('Dianthus barbatus')
if dianthusbarbatus:
	usrchoices.append('Dianthus barbatus')
dulichiumarundinaceum = st.checkbox('Dulichium arundinaceum')
if dulichiumarundinaceum:
	usrchoices.append('Dulichium arundinaceum')
echinaceapallida = st.checkbox('Echinacea pallida')
if echinaceapallida:
	usrchoices.append('Echinacea pallida')
echinaceapurpurea = st.checkbox('Echinacea purpurea')
if echinaceapurpurea:
	usrchoices.append('Echinacea purpurea')
elephantopuselatus = st.checkbox('Elephantopus elatus')
if elephantopuselatus:
	usrchoices.append('Elephantopus elatus')
elymuscanadensis = st.checkbox('Elymus canadensis')
if elymuscanadensis:
	usrchoices.append('Elymus canadensis')
elymushystrix = st.checkbox('Elymus hystrix')
if elymushystrix:
	usrchoices.append('Elymus hystrix')
elymusriparius = st.checkbox('Elymus riparius')
if elymusriparius:
	usrchoices.append('Elymus riparius')
elymusvirginicus = st.checkbox('Elymus virginicus')
if elymusvirginicus:
	usrchoices.append('Elymus virginicus')
eragrostiscurvula = st.checkbox('Eragrostis curvula')
if eragrostiscurvula:
	usrchoices.append('Eragrostis curvula')
eragrostiselliottii = st.checkbox('Eragrostis elliottii')
if eragrostiselliottii:
	usrchoices.append('Eragrostis elliottii')
eragrostishirsuta = st.checkbox('Eragrostis hirsuta')
if eragrostishirsuta:
	usrchoices.append('Eragrostis hirsuta')
eragrostisspectabilis = st.checkbox('Eragrostis spectabilis')
if eragrostisspectabilis:
	usrchoices.append('Eragrostis spectabilis')
eragrotistrichodes = st.checkbox('Eragrotis trichodes')
if eragrotistrichodes:
	usrchoices.append('Eragrotis trichodes')
erianthuscontortus = st.checkbox('Erianthus contortus')
if erianthuscontortus:
	usrchoices.append('Erianthus contortus')
eriophorumvirginicum = st.checkbox('Eriophorum virginicum')
if eriophorumvirginicum:
	usrchoices.append('Eriophorum virginicum')
eryngiumaquaticumvaraquaticum = st.checkbox('Eryngium aquaticum var. aquaticum')
if eryngiumaquaticumvaraquaticum:
	usrchoices.append('Eryngium aquaticum var. aquaticum')
eryngiumaquaticumvarravenelii = st.checkbox('Eryngium aquaticum var. ravenelii')
if eryngiumaquaticumvarravenelii:
	usrchoices.append('Eryngium aquaticum var. ravenelii')
eryngiumyuccifolium = st.checkbox('Eryngium yuccifolium')
if eryngiumyuccifolium:
	usrchoices.append('Eryngium yuccifolium')
eschscholziacalifornica = st.checkbox('Eschscholzia californica')
if eschscholziacalifornica:
	usrchoices.append('Eschscholzia californica')
eupatoriumcoelestinum = st.checkbox('Eupatorium coelestinum')
if eupatoriumcoelestinum:
	usrchoices.append('Eupatorium coelestinum')
eupatoriumfistulosum = st.checkbox('Eupatorium fistulosum')
if eupatoriumfistulosum:
	usrchoices.append('Eupatorium fistulosum')
eupatoriummaculatum = st.checkbox('Eupatorium maculatum')
if eupatoriummaculatum:
	usrchoices.append('Eupatorium maculatum')
eupatoriumperfoliatum = st.checkbox('Eupatorium perfoliatum')
if eupatoriumperfoliatum:
	usrchoices.append('Eupatorium perfoliatum')
eupatoriumpurpureum = st.checkbox('Eupatorium purpureum')
if eupatoriumpurpureum:
	usrchoices.append('Eupatorium purpureum')
eupatoriumrugosum = st.checkbox('Eupatorium rugosum')
if eupatoriumrugosum:
	usrchoices.append('Eupatorium rugosum')
euphorbiacorollata = st.checkbox('Euphorbia corollata')
if euphorbiacorollata:
	usrchoices.append('Euphorbia corollata')
euthamiacaroliniana = st.checkbox('Euthamia caroliniana')
if euthamiacaroliniana:
	usrchoices.append('Euthamia caroliniana')
euthamiagraminifolia = st.checkbox('Euthamia graminifolia')
if euthamiagraminifolia:
	usrchoices.append('Euthamia graminifolia')
festucaarundinacea = st.checkbox('Festuca arundinacea')
if festucaarundinacea:
	usrchoices.append('Festuca arundinacea')
festucaovinavarduriuscula = st.checkbox('Festuca ovina var. duriuscula')
if festucaovinavarduriuscula:
	usrchoices.append('Festuca ovina var. duriuscula')
festucaovinavarglauca = st.checkbox('Festuca ovina var. glauca')
if festucaovinavarglauca:
	usrchoices.append('Festuca ovina var. glauca')
festucaovina = st.checkbox('Festuca ovina')
if festucaovina:
	usrchoices.append('Festuca ovina')
festucarubrasspcommutata = st.checkbox('Festuca rubra ssp. commutata')
if festucarubrasspcommutata:
	usrchoices.append('Festuca rubra ssp. commutata')
festucarubra = st.checkbox('Festuca rubra')
if festucarubra:
	usrchoices.append('Festuca rubra')
gaillardiaaristata = st.checkbox('Gaillardia aristata')
if gaillardiaaristata:
	usrchoices.append('Gaillardia aristata')
gaillardiapulchella = st.checkbox('Gaillardia pulchella')
if gaillardiapulchella:
	usrchoices.append('Gaillardia pulchella')
gaurabiennis = st.checkbox('Gaura biennis')
if gaurabiennis:
	usrchoices.append('Gaura biennis')
gentianaclausa = st.checkbox('Gentiana clausa')
if gentianaclausa:
	usrchoices.append('Gentiana clausa')
geumcanadense = st.checkbox('Geum canadense')
if geumcanadense:
	usrchoices.append('Geum canadense')
glyceriacanadensis = st.checkbox('Glyceria canadensis')
if glyceriacanadensis:
	usrchoices.append('Glyceria canadensis')
glyceriagrandis = st.checkbox('Glyceria grandis')
if glyceriagrandis:
	usrchoices.append('Glyceria grandis')
glyceriaseptentrionalis = st.checkbox('Glyceria septentrionalis')
if glyceriaseptentrionalis:
	usrchoices.append('Glyceria septentrionalis')
glyceriastriata = st.checkbox('Glyceria striata')
if glyceriastriata:
	usrchoices.append('Glyceria striata')
gypsophilaelegans = st.checkbox('Gypsophila elegans')
if gypsophilaelegans:
	usrchoices.append('Gypsophila elegans')
heleniumautumnale = st.checkbox('Helenium autumnale')
if heleniumautumnale:
	usrchoices.append('Helenium autumnale')
heleniumflexuosum = st.checkbox('Helenium flexuosum')
if heleniumflexuosum:
	usrchoices.append('Helenium flexuosum')
helianthusangustifolius = st.checkbox('Helianthus angustifolius')
if helianthusangustifolius:
	usrchoices.append('Helianthus angustifolius')
helianthusannuus = st.checkbox('Helianthus annuus')
if helianthusannuus:
	usrchoices.append('Helianthus annuus')
helianthusgiganteus = st.checkbox('Helianthus giganteus')
if helianthusgiganteus:
	usrchoices.append('Helianthus giganteus')
helianthusmaximilianii = st.checkbox('Helianthus maximilianii')
if helianthusmaximilianii:
	usrchoices.append('Helianthus maximilianii')
helianthusoccidentalisvardowellianus = st.checkbox('Helianthus occidentalis var. dowellianus')
if helianthusoccidentalisvardowellianus:
	usrchoices.append('Helianthus occidentalis var. dowellianus')
helianthusradula = st.checkbox('Helianthus radula')
if helianthusradula:
	usrchoices.append('Helianthus radula')
heliopsishelianthoides = st.checkbox('Heliopsis helianthoides')
if heliopsishelianthoides:
	usrchoices.append('Heliopsis helianthoides')
hesperismatronalis = st.checkbox('Hesperis matronalis')
if hesperismatronalis:
	usrchoices.append('Hesperis matronalis')
hibiscusmoscheutos = st.checkbox('Hibiscus moscheutos')
if hibiscusmoscheutos:
	usrchoices.append('Hibiscus moscheutos')
hordeumjubatum = st.checkbox('Hordeum jubatum')
if hordeumjubatum:
	usrchoices.append('Hordeum jubatum')
hypericumperforatum = st.checkbox('Hypericum perforatum')
if hypericumperforatum:
	usrchoices.append('Hypericum perforatum')
hypericumpunctatum = st.checkbox('Hypericum punctatum')
if hypericumpunctatum:
	usrchoices.append('Hypericum punctatum')
hypericumpyramidatum = st.checkbox('Hypericum pyramidatum')
if hypericumpyramidatum:
	usrchoices.append('Hypericum pyramidatum')
irisversicolor = st.checkbox('Iris versicolor')
if irisversicolor:
	usrchoices.append('Iris versicolor')
irisvirginica = st.checkbox('Iris virginica')
if irisvirginica:
	usrchoices.append('Iris virginica')
juncuscanadensis = st.checkbox('Juncus canadensis')
if juncuscanadensis:
	usrchoices.append('Juncus canadensis')
juncuscoriaceus = st.checkbox('Juncus coriaceus')
if juncuscoriaceus:
	usrchoices.append('Juncus coriaceus')
juncuseffusus = st.checkbox('Juncus effusus')
if juncuseffusus:
	usrchoices.append('Juncus effusus')
juncustenuis = st.checkbox('Juncus tenuis')
if juncustenuis:
	usrchoices.append('Juncus tenuis')
juncustorreyi = st.checkbox('Juncus torreyi')
if juncustorreyi:
	usrchoices.append('Juncus torreyi')
khuniaeupatorioides = st.checkbox('Khunia eupatorioides')
if khuniaeupatorioides:
	usrchoices.append('Khunia eupatorioides')
koeleriamacrantha = st.checkbox('Koeleria macrantha')
if koeleriamacrantha:
	usrchoices.append('Koeleria macrantha')
kosteletzkyavirginica = st.checkbox('Kosteletzkya virginica')
if kosteletzkyavirginica:
	usrchoices.append('Kosteletzkya virginica')
lathyrussylvestris = st.checkbox('Lathyrus sylvestris')
if lathyrussylvestris:
	usrchoices.append('Lathyrus sylvestris')
lavateratrimestris = st.checkbox('Lavatera trimestris')
if lavateratrimestris:
	usrchoices.append('Lavatera trimestris')
leersiaoryzoides = st.checkbox('Leersia oryzoides')
if leersiaoryzoides:
	usrchoices.append('Leersia oryzoides')
lespedezabicolor = st.checkbox('Lespedeza bicolor')
if lespedezabicolor:
	usrchoices.append('Lespedeza bicolor')
lespedezacapitata = st.checkbox('Lespedeza capitata')
if lespedezacapitata:
	usrchoices.append('Lespedeza capitata')
lespedezacuneata = st.checkbox('Lespedeza cuneata')
if lespedezacuneata:
	usrchoices.append('Lespedeza cuneata')
lespedezafrutescens = st.checkbox('Lespedeza frutescens')
if lespedezafrutescens:
	usrchoices.append('Lespedeza frutescens')
lespedezastipulacea = st.checkbox('Lespedeza stipulacea')
if lespedezastipulacea:
	usrchoices.append('Lespedeza stipulacea')
lespedezavirginica = st.checkbox('Lespedeza virginica')
if lespedezavirginica:
	usrchoices.append('Lespedeza virginica')
liatrisaspera = st.checkbox('Liatris aspera')
if liatrisaspera:
	usrchoices.append('Liatris aspera')
liatriselegans = st.checkbox('Liatris elegans')
if liatriselegans:
	usrchoices.append('Liatris elegans')
liatrisgarberi = st.checkbox('Liatris garberi')
if liatrisgarberi:
	usrchoices.append('Liatris garberi')
liatrisgracilis = st.checkbox('Liatris gracilis')
if liatrisgracilis:
	usrchoices.append('Liatris gracilis')
liatrisgraminifolia = st.checkbox('Liatris graminifolia')
if liatrisgraminifolia:
	usrchoices.append('Liatris graminifolia')
liatrispycnostachya = st.checkbox('Liatris pycnostachya')
if liatrispycnostachya:
	usrchoices.append('Liatris pycnostachya')
liatrisspicata = st.checkbox('Liatris spicata')
if liatrisspicata:
	usrchoices.append('Liatris spicata')
liatrissquarrosa = st.checkbox('Liatris squarrosa')
if liatrissquarrosa:
	usrchoices.append('Liatris squarrosa')
liatrissquarrulosa = st.checkbox('Liatris squarrulosa')
if liatrissquarrulosa:
	usrchoices.append('Liatris squarrulosa')
liliumsuperbum = st.checkbox('Lilium superbum')
if liliumsuperbum:
	usrchoices.append('Lilium superbum')
linariamaroccana = st.checkbox('Linaria maroccana')
if linariamaroccana:
	usrchoices.append('Linaria maroccana')
linumgrandiflorumrubrum = st.checkbox('Linum grandiflorum rubrum')
if linumgrandiflorumrubrum:
	usrchoices.append('Linum grandiflorum rubrum')
linumperenne = st.checkbox('Linum perenne')
if linumperenne:
	usrchoices.append('Linum perenne')
linumusitatissimum = st.checkbox('Linum usitatissimum')
if linumusitatissimum:
	usrchoices.append('Linum usitatissimum')
lobeliacardinalis = st.checkbox('Lobelia cardinalis')
if lobeliacardinalis:
	usrchoices.append('Lobelia cardinalis')
lobeliapuberula = st.checkbox('Lobelia puberula')
if lobeliapuberula:
	usrchoices.append('Lobelia puberula')
lobeliasiphilitica = st.checkbox('Lobelia siphilitica')
if lobeliasiphilitica:
	usrchoices.append('Lobelia siphilitica')
lobulariamaritima = st.checkbox('Lobularia maritima')
if lobulariamaritima:
	usrchoices.append('Lobularia maritima')
loliummultiflorum = st.checkbox('Lolium multiflorum')
if loliummultiflorum:
	usrchoices.append('Lolium multiflorum')
loliumperenne = st.checkbox('Lolium perenne')
if loliumperenne:
	usrchoices.append('Lolium perenne')
lotuscorniculatus = st.checkbox('Lotus corniculatus')
if lotuscorniculatus:
	usrchoices.append('Lotus corniculatus')
ludwigiaalternifolia = st.checkbox('Ludwigia alternifolia')
if ludwigiaalternifolia:
	usrchoices.append('Ludwigia alternifolia')
ludwigialinearis = st.checkbox('Ludwigia linearis')
if ludwigialinearis:
	usrchoices.append('Ludwigia linearis')
ludwigiamaritima = st.checkbox('Ludwigia maritima')
if ludwigiamaritima:
	usrchoices.append('Ludwigia maritima')
lupinusperennis = st.checkbox('Lupinus perennis')
if lupinusperennis:
	usrchoices.append('Lupinus perennis')
lupinuspolyphyllus = st.checkbox('Lupinus polyphyllus')
if lupinuspolyphyllus:
	usrchoices.append('Lupinus polyphyllus')
lycopusamericanus = st.checkbox('Lycopus americanus')
if lycopusamericanus:
	usrchoices.append('Lycopus americanus')
melilotusofficinalis = st.checkbox('Melilotus officinalis')
if melilotusofficinalis:
	usrchoices.append('Melilotus officinalis')
mimulusringens = st.checkbox('Mimulus ringens')
if mimulusringens:
	usrchoices.append('Mimulus ringens')
monardafistulosa = st.checkbox('Monarda fistulosa')
if monardafistulosa:
	usrchoices.append('Monarda fistulosa')
monardamedia = st.checkbox('Monarda media')
if monardamedia:
	usrchoices.append('Monarda media')
monardapunctata = st.checkbox('Monarda punctata')
if monardapunctata:
	usrchoices.append('Monarda punctata')
muhlenbergiacapillaris = st.checkbox('Muhlenbergia capillaris')
if muhlenbergiacapillaris:
	usrchoices.append('Muhlenbergia capillaris')
muhlenbergiaschreberi = st.checkbox('Muhlenbergia schreberi')
if muhlenbergiaschreberi:
	usrchoices.append('Muhlenbergia schreberi')
oenotherabiennis = st.checkbox('Oenothera biennis')
if oenotherabiennis:
	usrchoices.append('Oenothera biennis')
oenotheraspeciosa = st.checkbox('Oenothera speciosa')
if oenotheraspeciosa:
	usrchoices.append('Oenothera speciosa')
onocleasensibilis = st.checkbox('Onoclea sensibilis')
if onocleasensibilis:
	usrchoices.append('Onoclea sensibilis')
panicumamarum = st.checkbox('Panicum amarum')
if panicumamarum:
	usrchoices.append('Panicum amarum')
panicumanceps = st.checkbox('Panicum anceps')
if panicumanceps:
	usrchoices.append('Panicum anceps')
panicumclandestinum = st.checkbox('Panicum clandestinum')
if panicumclandestinum:
	usrchoices.append('Panicum clandestinum')
panicumdichotomiflorum = st.checkbox('Panicum dichotomiflorum')
if panicumdichotomiflorum:
	usrchoices.append('Panicum dichotomiflorum')
panicumrigidulum = st.checkbox('Panicum rigidulum')
if panicumrigidulum:
	usrchoices.append('Panicum rigidulum')
panicumvirgatum = st.checkbox('Panicum virgatum')
if panicumvirgatum:
	usrchoices.append('Panicum virgatum')
papavernudicale = st.checkbox('Papaver nudicale')
if papavernudicale:
	usrchoices.append('Papaver nudicale')
papaverrhoeas = st.checkbox('Papaver rhoeas')
if papaverrhoeas:
	usrchoices.append('Papaver rhoeas')
partheniumintegrifolium = st.checkbox('Parthenium integrifolium ')
if partheniumintegrifolium:
	usrchoices.append('Parthenium integrifolium ')
peltandravirginica = st.checkbox('Peltandra virginica')
if peltandravirginica:
	usrchoices.append('Peltandra virginica')
penstemonaustralis = st.checkbox('Penstemon australis')
if penstemonaustralis:
	usrchoices.append('Penstemon australis')
penstemondigitalis = st.checkbox('Penstemon digitalis')
if penstemondigitalis:
	usrchoices.append('Penstemon digitalis')
penstemonhirsutus = st.checkbox('Penstemon hirsutus')
if penstemonhirsutus:
	usrchoices.append('Penstemon hirsutus')
penstemonlaevigatus = st.checkbox('Penstemon laevigatus')
if penstemonlaevigatus:
	usrchoices.append('Penstemon laevigatus')
penstemonmultiflorus = st.checkbox('Penstemon multiflorus')
if penstemonmultiflorus:
	usrchoices.append('Penstemon multiflorus')
penthorumsedoides = st.checkbox('Penthorum sedoides')
if penthorumsedoides:
	usrchoices.append('Penthorum sedoides')
phaceliacampanularia = st.checkbox('Phacelia campanularia')
if phaceliacampanularia:
	usrchoices.append('Phacelia campanularia')
phalarisarundinacea = st.checkbox('Phalaris arundinacea')
if phalarisarundinacea:
	usrchoices.append('Phalaris arundinacea')
phleumpratense = st.checkbox('Phleum pratense')
if phleumpratense:
	usrchoices.append('Phleum pratense')
poacompressa = st.checkbox('Poa compressa')
if poacompressa:
	usrchoices.append('Poa compressa')
poapalustris = st.checkbox('Poa palustris')
if poapalustris:
	usrchoices.append('Poa palustris')
poapratensis = st.checkbox('Poa pratensis')
if poapratensis:
	usrchoices.append('Poa pratensis')
poatrivialis = st.checkbox('Poa trivialis')
if poatrivialis:
	usrchoices.append('Poa trivialis')
polygonumpensylvanicum = st.checkbox('Polygonum pensylvanicum')
if polygonumpensylvanicum:
	usrchoices.append('Polygonum pensylvanicum')
polygonumsagittatum = st.checkbox('Polygonum sagittatum')
if polygonumsagittatum:
	usrchoices.append('Polygonum sagittatum')
pontederiacordata = st.checkbox('Pontederia cordata')
if pontederiacordata:
	usrchoices.append('Pontederia cordata')
puccinelliadistans = st.checkbox('Puccinellia distans')
if puccinelliadistans:
	usrchoices.append('Puccinellia distans')
puccinellianuttalliana = st.checkbox('Puccinellia nuttalliana')
if puccinellianuttalliana:
	usrchoices.append('Puccinellia nuttalliana')
pycnanthemumincanum = st.checkbox('Pycnanthemum incanum')
if pycnanthemumincanum:
	usrchoices.append('Pycnanthemum incanum')
pycnanthemummuticum = st.checkbox('Pycnanthemum muticum')
if pycnanthemummuticum:
	usrchoices.append('Pycnanthemum muticum')
pycnanthemumtenuifolium = st.checkbox('Pycnanthemum tenuifolium')
if pycnanthemumtenuifolium:
	usrchoices.append('Pycnanthemum tenuifolium')
pycnanthemumvirginianum = st.checkbox('Pycnanthemum virginianum')
if pycnanthemumvirginianum:
	usrchoices.append('Pycnanthemum virginianum')
ratibidacolumnaris = st.checkbox('Ratibida columnaris')
if ratibidacolumnaris:
	usrchoices.append('Ratibida columnaris')
ratibidacolumnifera = st.checkbox('Ratibida columnifera')
if ratibidacolumnifera:
	usrchoices.append('Ratibida columnifera')
ratibidapinnata = st.checkbox('Ratibida pinnata')
if ratibidapinnata:
	usrchoices.append('Ratibida pinnata')
rhexiamariana = st.checkbox('Rhexia mariana')
if rhexiamariana:
	usrchoices.append('Rhexia mariana')
rhexiavirginica = st.checkbox('Rhexia virginica')
if rhexiavirginica:
	usrchoices.append('Rhexia virginica')
rhynchosporaglobularis = st.checkbox('Rhynchospora globularis')
if rhynchosporaglobularis:
	usrchoices.append('Rhynchospora globularis')
rudbeckiaamplexicaulis = st.checkbox('Rudbeckia amplexicaulis')
if rudbeckiaamplexicaulis:
	usrchoices.append('Rudbeckia amplexicaulis')
rudbeckiafulgida = st.checkbox('Rudbeckia fulgida')
if rudbeckiafulgida:
	usrchoices.append('Rudbeckia fulgida')
rudbeckiahirta = st.checkbox('Rudbeckia hirta')
if rudbeckiahirta:
	usrchoices.append('Rudbeckia hirta')
rudbeckialaciniata = st.checkbox('Rudbeckia laciniata')
if rudbeckialaciniata:
	usrchoices.append('Rudbeckia laciniata')
rudbeckiamohrii = st.checkbox('Rudbeckia mohrii')
if rudbeckiamohrii:
	usrchoices.append('Rudbeckia mohrii')
rudbeckianitida = st.checkbox('Rudbeckia nitida')
if rudbeckianitida:
	usrchoices.append('Rudbeckia nitida')
rudbeckiasubtomentosa = st.checkbox('Rudbeckia subtomentosa')
if rudbeckiasubtomentosa:
	usrchoices.append('Rudbeckia subtomentosa')
rudbeckiatriloba = st.checkbox('Rudbeckia triloba')
if rudbeckiatriloba:
	usrchoices.append('Rudbeckia triloba')
sagittarialatifolia = st.checkbox('Sagittaria latifolia')
if sagittarialatifolia:
	usrchoices.append('Sagittaria latifolia')
saururuscernuus = st.checkbox('Saururus cernuus')
if saururuscernuus:
	usrchoices.append('Saururus cernuus')
schizachyriumscoparium = st.checkbox('Schizachyrium scoparium')
if schizachyriumscoparium:
	usrchoices.append('Schizachyrium scoparium')
scirpusacutus = st.checkbox('Scirpus acutus')
if scirpusacutus:
	usrchoices.append('Scirpus acutus')
scirpusatrovirens = st.checkbox('Scirpus atrovirens')
if scirpusatrovirens:
	usrchoices.append('Scirpus atrovirens')
scirpuscyperinus = st.checkbox('Scirpus cyperinus')
if scirpuscyperinus:
	usrchoices.append('Scirpus cyperinus')
scirpusexpansus = st.checkbox('Scirpus expansus')
if scirpusexpansus:
	usrchoices.append('Scirpus expansus')
scirpuspendulus = st.checkbox('Scirpus pendulus')
if scirpuspendulus:
	usrchoices.append('Scirpus pendulus')
scirpuspolyphyllus = st.checkbox('Scirpus polyphyllus')
if scirpuspolyphyllus:
	usrchoices.append('Scirpus polyphyllus')
scirpusrobustus = st.checkbox('Scirpus robustus')
if scirpusrobustus:
	usrchoices.append('Scirpus robustus')
scirpusvalidus = st.checkbox('Scirpus validus')
if scirpusvalidus:
	usrchoices.append('Scirpus validus')
scutellariaincana = st.checkbox('Scutellaria incana')
if scutellariaincana:
	usrchoices.append('Scutellaria incana')
sennahebecarpa = st.checkbox('Senna hebecarpa')
if sennahebecarpa:
	usrchoices.append('Senna hebecarpa')
sennamarilandica = st.checkbox('Senna marilandica')
if sennamarilandica:
	usrchoices.append('Senna marilandica')
silenearmeria = st.checkbox('Silene armeria')
if silenearmeria:
	usrchoices.append('Silene armeria')
silphiumasteriscusvarangustatum = st.checkbox('Silphium asteriscus var. angustatum')
if silphiumasteriscusvarangustatum:
	usrchoices.append('Silphium asteriscus var. angustatum')
silphiumasteriscusvarlaevicaule = st.checkbox('Silphium asteriscus var. laevicaule')
if silphiumasteriscusvarlaevicaule:
	usrchoices.append('Silphium asteriscus var. laevicaule')
silphiumintegrifolium = st.checkbox('Silphium integrifolium')
if silphiumintegrifolium:
	usrchoices.append('Silphium integrifolium')
silphiumlaciniatum = st.checkbox('Silphium laciniatum')
if silphiumlaciniatum:
	usrchoices.append('Silphium laciniatum')
silphiumperfoliatum = st.checkbox('Silphium perfoliatum')
if silphiumperfoliatum:
	usrchoices.append('Silphium perfoliatum')
silphiumterebinthaceum = st.checkbox('Silphium terebinthaceum')
if silphiumterebinthaceum:
	usrchoices.append('Silphium terebinthaceum')
silphiumtrifoliatum = st.checkbox('Silphium trifoliatum')
if silphiumtrifoliatum:
	usrchoices.append('Silphium trifoliatum')
sisyrinchiumangustifolium = st.checkbox('Sisyrinchium angustifolium')
if sisyrinchiumangustifolium:
	usrchoices.append('Sisyrinchium angustifolium')
solidagobicolor = st.checkbox('Solidago bicolor')
if solidagobicolor:
	usrchoices.append('Solidago bicolor')
solidagocaesia = st.checkbox('Solidago caesia')
if solidagocaesia:
	usrchoices.append('Solidago caesia')
solidagocanadensis = st.checkbox('Solidago canadensis')
if solidagocanadensis:
	usrchoices.append('Solidago canadensis')
solidagofistulosa = st.checkbox('Solidago fistulosa')
if solidagofistulosa:
	usrchoices.append('Solidago fistulosa')
solidagoflexicaulis = st.checkbox('Solidago flexicaulis')
if solidagoflexicaulis:
	usrchoices.append('Solidago flexicaulis')
solidagojuncea = st.checkbox('Solidago juncea')
if solidagojuncea:
	usrchoices.append('Solidago juncea')
solidagonemoralis = st.checkbox('Solidago nemoralis')
if solidagonemoralis:
	usrchoices.append('Solidago nemoralis')
solidagoodora = st.checkbox('Solidago odora')
if solidagoodora:
	usrchoices.append('Solidago odora')
solidagopatula = st.checkbox('Solidago patula')
if solidagopatula:
	usrchoices.append('Solidago patula')
solidagoriddellii = st.checkbox('Solidago riddellii')
if solidagoriddellii:
	usrchoices.append('Solidago riddellii')
solidagorigida = st.checkbox('Solidago rigida')
if solidagorigida:
	usrchoices.append('Solidago rigida')
solidagorugosa = st.checkbox('Solidago rugosa')
if solidagorugosa:
	usrchoices.append('Solidago rugosa')
solidagosempervirens = st.checkbox('Solidago sempervirens')
if solidagosempervirens:
	usrchoices.append('Solidago sempervirens')
solidagospeciosa = st.checkbox('Solidago speciosa')
if solidagospeciosa:
	usrchoices.append('Solidago speciosa')
solidagostricta = st.checkbox('Solidago stricta')
if solidagostricta:
	usrchoices.append('Solidago stricta')
sorghastrumelliotti = st.checkbox('Sorghastrum elliotti')
if sorghastrumelliotti:
	usrchoices.append('Sorghastrum elliotti')
sorghastrumnutans = st.checkbox('Sorghastrum nutans')
if sorghastrumnutans:
	usrchoices.append('Sorghastrum nutans')
sorghastrumsecundum = st.checkbox('Sorghastrum secundum')
if sorghastrumsecundum:
	usrchoices.append('Sorghastrum secundum')
sparganiumamericanum = st.checkbox('Sparganium americanum')
if sparganiumamericanum:
	usrchoices.append('Sparganium americanum')
sparganiumeurycarpum = st.checkbox('Sparganium eurycarpum')
if sparganiumeurycarpum:
	usrchoices.append('Sparganium eurycarpum')
spartinapectinata = st.checkbox('Spartina pectinata')
if spartinapectinata:
	usrchoices.append('Spartina pectinata')
sporobolusasper = st.checkbox('Sporobolus asper')
if sporobolusasper:
	usrchoices.append('Sporobolus asper')
sporoboluscryptandrus = st.checkbox('Sporobolus cryptandrus')
if sporoboluscryptandrus:
	usrchoices.append('Sporobolus cryptandrus')
sporobolusheterolepis = st.checkbox('Sporobolus heterolepis')
if sporobolusheterolepis:
	usrchoices.append('Sporobolus heterolepis')
sporobolusjunceus = st.checkbox('Sporobolus junceus')
if sporobolusjunceus:
	usrchoices.append('Sporobolus junceus')
thalictrumpubescens = st.checkbox('Thalictrum pubescens')
if thalictrumpubescens:
	usrchoices.append('Thalictrum pubescens')
tradescantiaohiensis = st.checkbox('Tradescantia ohiensis')
if tradescantiaohiensis:
	usrchoices.append('Tradescantia ohiensis')
tradescantiasubaspera = st.checkbox('Tradescantia subaspera')
if tradescantiasubaspera:
	usrchoices.append('Tradescantia subaspera')
tradescantiavirginiana = st.checkbox('Tradescantia virginiana')
if tradescantiavirginiana:
	usrchoices.append('Tradescantia virginiana')
tridensflavus = st.checkbox('Tridens flavus')
if tridensflavus:
	usrchoices.append('Tridens flavus')
trifoliumhybridum = st.checkbox('Trifolium hybridum')
if trifoliumhybridum:
	usrchoices.append('Trifolium hybridum')
trifoliumincarnatum = st.checkbox('Trifolium incarnatum')
if trifoliumincarnatum:
	usrchoices.append('Trifolium incarnatum')
trifoliumpratense = st.checkbox('Trifolium pratense')
if trifoliumpratense:
	usrchoices.append('Trifolium pratense')
trifoliumrepens = st.checkbox('Trifolium repens')
if trifoliumrepens:
	usrchoices.append('Trifolium repens')
tripsacumdactyloides = st.checkbox('Tripsacum dactyloides')
if tripsacumdactyloides:
	usrchoices.append('Tripsacum dactyloides')
typhaangustifolia = st.checkbox('Typha angustifolia')
if typhaangustifolia:
	usrchoices.append('Typha angustifolia')
typhalatifolia = st.checkbox('Typha latifolia')
if typhalatifolia:
	usrchoices.append('Typha latifolia')
veratrumviride = st.checkbox('Veratrum viride')
if veratrumviride:
	usrchoices.append('Veratrum viride')
verbenahastata = st.checkbox('Verbena hastata')
if verbenahastata:
	usrchoices.append('Verbena hastata')
verbenastricta = st.checkbox('Verbena stricta')
if verbenastricta:
	usrchoices.append('Verbena stricta')
verbenaurticifolia = st.checkbox('Verbena urticifolia')
if verbenaurticifolia:
	usrchoices.append('Verbena urticifolia')
verbesinaalternifolia = st.checkbox('Verbesina alternifolia')
if verbesinaalternifolia:
	usrchoices.append('Verbesina alternifolia')
vernoniaacaulis = st.checkbox('Vernonia acaulis')
if vernoniaacaulis:
	usrchoices.append('Vernonia acaulis')
vernoniaangustifolia = st.checkbox('Vernonia angustifolia')
if vernoniaangustifolia:
	usrchoices.append('Vernonia angustifolia')
vernoniagigantea = st.checkbox('Vernonia gigantea')
if vernoniagigantea:
	usrchoices.append('Vernonia gigantea')
vernonianoveboracensis = st.checkbox('Vernonia noveboracensis')
if vernonianoveboracensis:
	usrchoices.append('Vernonia noveboracensis')
veronicastrumvirginicum = st.checkbox('Veronicastrum virginicum')
if veronicastrumvirginicum:
	usrchoices.append('Veronicastrum virginicum')
violacornuta = st.checkbox('Viola cornuta')
if violacornuta:
	usrchoices.append('Viola cornuta')
ziziaaurea = st.checkbox('Zizia aurea')
if ziziaaurea:
	usrchoices.append('Zizia aurea')
zizaniaaquatica = st.checkbox('Zizania aquatica')
if zizaniaaquatica:
	usrchoices.append('Zizania aquatica')


st.write("You chose:", usrchoices)

#this creates the dataframe that has only your user's choices in it
seedchoices = SEEDLIST[SEEDLIST['species'].isin(usrchoices)]

#TODO: add code that lets the user input plants/meter for each of their
#choices and creates a new DF with 2 columns: "species", "plantsper"

st.write("Here is an example of the graphing from your sample data:")

#read in the data (this will be replaced by TODO code above)
choices_raw = DATA = pd.read_csv("../sampledocs/seedcount_SampleOutput.csv",
                                 header=0,
                                 index_col=False,
                                 names=['species', 'common_name', 'plantsper', 'germ_rate', 'lbs',
                                        'perc_lb', 'forb', 'fall'])

choices = choices_raw[["species", "common_name", "plantsper"]]

#this for loop generates the plotting data
species = []
x = []
y = []
for index, row in choices.iterrows():
    for i in range (1, row['plantsper']):
        species.append(row["species"])
        x.append(random.uniform(0, 1))
        y.append(random.uniform(0, 1))
metercalc = pd.DataFrame(list(zip(species, x, y)), columns=["species", "x", "y"])

#build the altair chart

#define datasource 
source = metercalc
#interactive highlight function
highlight = alt.selection(type='single',
                          fields=['species'], empty="all")
#color
color = alt.condition(highlight,
                      alt.Color('species:N', scale=alt.Scale(scheme='spectral')),
                      alt.value('lightgray'))

#define the altair chart
visualizeseeds = alt.Chart(source).mark_point(filled=True, size=100).encode(
    x='x',
    y='y',
    color=color,
    tooltip=['species:N']
).add_selection(
    highlight
)

#call altair chart with streamlit
st.altair_chart(visualizeseeds, use_container_width=True)
