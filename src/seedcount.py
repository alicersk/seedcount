#!usr/bin/env python

import streamlit as st
import pandas as pd
import random
import altair as alt


#To run, paste into terminal: streamlit run seedcount.py

"""
# Seed Count
Here are all the species you have to choose from! 
Please enter the number of plants per square meter you'd like to see for each species you select.
I'm sorry, there is a lot of scrolling involved right now. The fun stuff is way at the bottom.
"""

#create empty dictionary to store choices
usrchoices = {}

#Loading CSV with pandas
labeled_data = pd.read_csv('SEEDS.csv')

#This function takes in the alphabet input from the sidebar and returns a subset of dataframe
def alphabet_choosing(letter):
	a1 = labeled_data.copy(deep = True)
	a1 = a1[a1['species'].str[0] == letter]
	return a1

#Sidebar for selecting alphabet
add_label = st.sidebar.selectbox("Choose an alphabet",('ALL','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'))

#Alphabetical selections
if add_label == "ALL":
	chosen_alphabet = labeled_data
else:
	chosen_alphabet = alphabet_choosing(add_label)


count = 0
#Displaying the options to 
for x in chosen_alphabet['species']:
	unique_key = x + str (count)
	options = st.number_input(x,min_value=0, max_value=500, step=1, key=unique_key)
	count +=1
if options:
	usrchoices[x] = options


#make the choices using checkboxes
	#this code is copy-pasted from "checkboxes.txt" and was generated with 'makeboxes.py'
	#I think there is a much more elegant way to do this, but I did want to see
	#if you could use checkboxes instead of the drop-down menu, which is not my
	#personal preferred way of making choices
# achilleamillefolium = st.number_input('Achillea millefolium', min_value=0, max_value=500, step=1)
# if achilleamillefolium:
# 	usrchoices['Achillea millefolium']=achilleamillefolium
# acorusamericanus = st.number_input('Acorus americanus', min_value=0, max_value=500, step=1)
# if acorusamericanus:
# 	usrchoices['Acorus americanus']=acorusamericanus
# agastachefoeniculum = st.number_input('Agastache foeniculum', min_value=0, max_value=500, step=1)
# if agastachefoeniculum:
# 	usrchoices['Agastache foeniculum']=agastachefoeniculum
# agrimoniaparviflora = st.number_input('Agrimonia parviflora', min_value=0, max_value=500, step=1)
# if agrimoniaparviflora:
# 	usrchoices['Agrimonia parviflora']=agrimoniaparviflora
# agrostisalba = st.number_input('Agrostis alba', min_value=0, max_value=500, step=1)
# if agrostisalba:
# 	usrchoices['Agrostis alba']=agrostisalba
# agrostishyemalis = st.number_input('Agrostis hyemalis', min_value=0, max_value=500, step=1)
# if agrostishyemalis:
# 	usrchoices['Agrostis hyemalis']=agrostishyemalis
# agrostisperennans = st.number_input('Agrostis perennans', min_value=0, max_value=500, step=1)
# if agrostisperennans:
# 	usrchoices['Agrostis perennans']=agrostisperennans
# agrostisscabra = st.number_input('Agrostis scabra', min_value=0, max_value=500, step=1)
# if agrostisscabra:
# 	usrchoices['Agrostis scabra']=agrostisscabra
# agrostisstolonifera = st.number_input('Agrostis stolonifera', min_value=0, max_value=500, step=1)
# if agrostisstolonifera:
# 	usrchoices['Agrostis stolonifera']=agrostisstolonifera
# agrostistenuis = st.number_input('Agrostis tenuis', min_value=0, max_value=500, step=1)
# if agrostistenuis:
# 	usrchoices['Agrostis tenuis']=agrostistenuis
# alismasubcordatum = st.number_input('Alisma subcordatum', min_value=0, max_value=500, step=1)
# if alismasubcordatum:
# 	usrchoices['Alisma subcordatum']=alismasubcordatum
# alliumcernuum = st.number_input('Allium cernuum', min_value=0, max_value=500, step=1)
# if alliumcernuum:
# 	usrchoices['Allium cernuum']=alliumcernuum
# alopecurusarundianceus = st.number_input('Alopecurus arundianceus', min_value=0, max_value=500, step=1)
# if alopecurusarundianceus:
# 	usrchoices['Alopecurus arundianceus']=alopecurusarundianceus
# ammimajus = st.number_input('Ammi majus', min_value=0, max_value=500, step=1)
# if ammimajus:
# 	usrchoices['Ammi majus']=ammimajus
# amorphacanescens = st.number_input('Amorpha canescens', min_value=0, max_value=500, step=1)
# if amorphacanescens:
# 	usrchoices['Amorpha canescens']=amorphacanescens
# amorphafruticosa = st.number_input('Amorpha fruticosa', min_value=0, max_value=500, step=1)
# if amorphafruticosa:
# 	usrchoices['Amorpha fruticosa']=amorphafruticosa
# amorphaherbacea = st.number_input('Amorpha herbacea', min_value=0, max_value=500, step=1)
# if amorphaherbacea:
# 	usrchoices['Amorpha herbacea']=amorphaherbacea
# amsoniaciliata = st.number_input('Amsonia ciliata', min_value=0, max_value=500, step=1)
# if amsoniaciliata:
# 	usrchoices['Amsonia ciliata']=amsoniaciliata
# andropogongerardii = st.number_input('Andropogon gerardii', min_value=0, max_value=500, step=1)
# if andropogongerardii:
# 	usrchoices['Andropogon gerardii']=andropogongerardii
# andropogonglomeratus = st.number_input('Andropogon glomeratus ', min_value=0, max_value=500, step=1)
# if andropogonglomeratus:
# 	usrchoices['Andropogon glomeratus ']=andropogonglomeratus
# andropogonglomeratusvarglaucopsis = st.number_input('Andropogon glomeratus var. glaucopsis', min_value=0, max_value=500, step=1)
# if andropogonglomeratusvarglaucopsis:
# 	usrchoices['Andropogon glomeratus var. glaucopsis']=andropogonglomeratusvarglaucopsis
# andropogonternarius = st.number_input('Andropogon ternarius', min_value=0, max_value=500, step=1)
# if andropogonternarius:
# 	usrchoices['Andropogon ternarius']=andropogonternarius
# andropogonvirginicus = st.number_input('Andropogon virginicus', min_value=0, max_value=500, step=1)
# if andropogonvirginicus:
# 	usrchoices['Andropogon virginicus']=andropogonvirginicus
# anemonecanadensis = st.number_input('Anemone canadensis', min_value=0, max_value=500, step=1)
# if anemonecanadensis:
# 	usrchoices['Anemone canadensis']=anemonecanadensis
# anemonevirginiana = st.number_input('Anemone virginiana', min_value=0, max_value=500, step=1)
# if anemonevirginiana:
# 	usrchoices['Anemone virginiana']=anemonevirginiana
# apocynumcannabinum = st.number_input('Apocynum cannabinum', min_value=0, max_value=500, step=1)
# if apocynumcannabinum:
# 	usrchoices['Apocynum cannabinum']=apocynumcannabinum
# aquilegiacanadensis = st.number_input('Aquilegia canadensis', min_value=0, max_value=500, step=1)
# if aquilegiacanadensis:
# 	usrchoices['Aquilegia canadensis']=aquilegiacanadensis
# asclepiasincarnata = st.number_input('Asclepias incarnata', min_value=0, max_value=500, step=1)
# if asclepiasincarnata:
# 	usrchoices['Asclepias incarnata']=asclepiasincarnata
# asclepiassyriaca = st.number_input('Asclepias syriaca', min_value=0, max_value=500, step=1)
# if asclepiassyriaca:
# 	usrchoices['Asclepias syriaca']=asclepiassyriaca
# asclepiastuberosa = st.number_input('Asclepias tuberosa', min_value=0, max_value=500, step=1)
# if asclepiastuberosa:
# 	usrchoices['Asclepias tuberosa']=asclepiastuberosa
# asterdivaricatus = st.number_input('Aster divaricatus', min_value=0, max_value=500, step=1)
# if asterdivaricatus:
# 	usrchoices['Aster divaricatus']=asterdivaricatus
# asterlaevis = st.number_input('Aster laevis', min_value=0, max_value=500, step=1)
# if asterlaevis:
# 	usrchoices['Aster laevis']=asterlaevis
# asterlowrieanus = st.number_input('Aster lowrieanus', min_value=0, max_value=500, step=1)
# if asterlowrieanus:
# 	usrchoices['Aster lowrieanus']=asterlowrieanus
# astermacrophyllus = st.number_input('Aster macrophyllus', min_value=0, max_value=500, step=1)
# if astermacrophyllus:
# 	usrchoices['Aster macrophyllus']=astermacrophyllus
# asternovaeangliae = st.number_input('Aster novae-angliae', min_value=0, max_value=500, step=1)
# if asternovaeangliae:
# 	usrchoices['Aster novae-angliae']=asternovaeangliae
# asternovibelgii = st.number_input('Aster novi-belgii', min_value=0, max_value=500, step=1)
# if asternovibelgii:
# 	usrchoices['Aster novi-belgii']=asternovibelgii
# asteroblongifolius = st.number_input('Aster oblongifolius', min_value=0, max_value=500, step=1)
# if asteroblongifolius:
# 	usrchoices['Aster oblongifolius']=asteroblongifolius
# asterpatens = st.number_input('Aster patens', min_value=0, max_value=500, step=1)
# if asterpatens:
# 	usrchoices['Aster patens']=asterpatens
# asterpilosus = st.number_input('Aster pilosus', min_value=0, max_value=500, step=1)
# if asterpilosus:
# 	usrchoices['Aster pilosus']=asterpilosus
# asterprenanthoides = st.number_input('Aster prenanthoides', min_value=0, max_value=500, step=1)
# if asterprenanthoides:
# 	usrchoices['Aster prenanthoides']=asterprenanthoides
# asterpuniceus = st.number_input('Aster puniceus', min_value=0, max_value=500, step=1)
# if asterpuniceus:
# 	usrchoices['Aster puniceus']=asterpuniceus
# astersagittifolius = st.number_input('Aster sagittifolius', min_value=0, max_value=500, step=1)
# if astersagittifolius:
# 	usrchoices['Aster sagittifolius']=astersagittifolius
# asterspectabilis = st.number_input('Aster spectabilis', min_value=0, max_value=500, step=1)
# if asterspectabilis:
# 	usrchoices['Aster spectabilis']=asterspectabilis
# asterumbellatus = st.number_input('Aster umbellatus', min_value=0, max_value=500, step=1)
# if asterumbellatus:
# 	usrchoices['Aster umbellatus']=asterumbellatus
# baptisiaalba = st.number_input('Baptisia alba', min_value=0, max_value=500, step=1)
# if baptisiaalba:
# 	usrchoices['Baptisia alba']=baptisiaalba
# baptisiaalbescens = st.number_input('Baptisia albescens', min_value=0, max_value=500, step=1)
# if baptisiaalbescens:
# 	usrchoices['Baptisia albescens']=baptisiaalbescens
# baptisiaaustralis = st.number_input('Baptisia australis', min_value=0, max_value=500, step=1)
# if baptisiaaustralis:
# 	usrchoices['Baptisia australis']=baptisiaaustralis
# baptisiacinerea = st.number_input('Baptisia cinerea', min_value=0, max_value=500, step=1)
# if baptisiacinerea:
# 	usrchoices['Baptisia cinerea']=baptisiacinerea
# baptisiapendula = st.number_input('Baptisia pendula', min_value=0, max_value=500, step=1)
# if baptisiapendula:
# 	usrchoices['Baptisia pendula']=baptisiapendula
# baptisiaperfoliata = st.number_input('Baptisia perfoliata', min_value=0, max_value=500, step=1)
# if baptisiaperfoliata:
# 	usrchoices['Baptisia perfoliata']=baptisiaperfoliata
# baptisiatinctoria = st.number_input('Baptisia tinctoria', min_value=0, max_value=500, step=1)
# if baptisiatinctoria:
# 	usrchoices['Baptisia tinctoria']=baptisiatinctoria
# bidensaristosa = st.number_input('Bidens aristosa', min_value=0, max_value=500, step=1)
# if bidensaristosa:
# 	usrchoices['Bidens aristosa']=bidensaristosa
# bidenscernua = st.number_input('Bidens cernua', min_value=0, max_value=500, step=1)
# if bidenscernua:
# 	usrchoices['Bidens cernua']=bidenscernua
# bidensfrondosa = st.number_input('Bidens frondosa', min_value=0, max_value=500, step=1)
# if bidensfrondosa:
# 	usrchoices['Bidens frondosa']=bidensfrondosa
# blephiliaciliata = st.number_input('Blephilia ciliata', min_value=0, max_value=500, step=1)
# if blephiliaciliata:
# 	usrchoices['Blephilia ciliata']=blephiliaciliata
# boltoniaasteroides = st.number_input('Boltonia asteroides', min_value=0, max_value=500, step=1)
# if boltoniaasteroides:
# 	usrchoices['Boltonia asteroides']=boltoniaasteroides
# boutelouacurtipendula = st.number_input('Bouteloua curtipendula', min_value=0, max_value=500, step=1)
# if boutelouacurtipendula:
# 	usrchoices['Bouteloua curtipendula']=boutelouacurtipendula
# boutelouagracilis = st.number_input('Bouteloua gracilis', min_value=0, max_value=500, step=1)
# if boutelouagracilis:
# 	usrchoices['Bouteloua gracilis']=boutelouagracilis
# bromusinermis = st.number_input('Bromus inermis', min_value=0, max_value=500, step=1)
# if bromusinermis:
# 	usrchoices['Bromus inermis']=bromusinermis
# buchloedactyloides = st.number_input('Buchloe dactyloides', min_value=0, max_value=500, step=1)
# if buchloedactyloides:
# 	usrchoices['Buchloe dactyloides']=buchloedactyloides
# calamagrostiscanadensis = st.number_input('Calamagrostis canadensis', min_value=0, max_value=500, step=1)
# if calamagrostiscanadensis:
# 	usrchoices['Calamagrostis canadensis']=calamagrostiscanadensis
# calendulaofficinalis = st.number_input('Calendula officinalis', min_value=0, max_value=500, step=1)
# if calendulaofficinalis:
# 	usrchoices['Calendula officinalis']=calendulaofficinalis
# carexalata = st.number_input('Carex alata', min_value=0, max_value=500, step=1)
# if carexalata:
# 	usrchoices['Carex alata']=carexalata
# carexalbolutescens = st.number_input('Carex albolutescens', min_value=0, max_value=500, step=1)
# if carexalbolutescens:
# 	usrchoices['Carex albolutescens']=carexalbolutescens
# carexcomosa = st.number_input('Carex comosa', min_value=0, max_value=500, step=1)
# if carexcomosa:
# 	usrchoices['Carex comosa']=carexcomosa
# carexcrinita = st.number_input('Carex crinita', min_value=0, max_value=500, step=1)
# if carexcrinita:
# 	usrchoices['Carex crinita']=carexcrinita
# carexfolliculata = st.number_input('Carex folliculata', min_value=0, max_value=500, step=1)
# if carexfolliculata:
# 	usrchoices['Carex folliculata']=carexfolliculata
# carexfrankii = st.number_input('Carex frankii', min_value=0, max_value=500, step=1)
# if carexfrankii:
# 	usrchoices['Carex frankii']=carexfrankii
# carexglaucescens = st.number_input('Carex glaucescens', min_value=0, max_value=500, step=1)
# if carexglaucescens:
# 	usrchoices['Carex glaucescens']=carexglaucescens
# carexgranularisvarhaleana = st.number_input('Carex granularis var. haleana', min_value=0, max_value=500, step=1)
# if carexgranularisvarhaleana:
# 	usrchoices['Carex granularis var. haleana']=carexgranularisvarhaleana
# carexgrayi = st.number_input('Carex grayi', min_value=0, max_value=500, step=1)
# if carexgrayi:
# 	usrchoices['Carex grayi']=carexgrayi
# carexgynandra = st.number_input('Carex gynandra', min_value=0, max_value=500, step=1)
# if carexgynandra:
# 	usrchoices['Carex gynandra']=carexgynandra
# carexintumescens = st.number_input('Carex intumescens', min_value=0, max_value=500, step=1)
# if carexintumescens:
# 	usrchoices['Carex intumescens']=carexintumescens
# carexlacustris = st.number_input('Carex lacustris', min_value=0, max_value=500, step=1)
# if carexlacustris:
# 	usrchoices['Carex lacustris']=carexlacustris
# carexlupulina = st.number_input('Carex lupulina', min_value=0, max_value=500, step=1)
# if carexlupulina:
# 	usrchoices['Carex lupulina']=carexlupulina
# carexlurida = st.number_input('Carex lurida', min_value=0, max_value=500, step=1)
# if carexlurida:
# 	usrchoices['Carex lurida']=carexlurida
# carexscoparia = st.number_input('Carex scoparia', min_value=0, max_value=500, step=1)
# if carexscoparia:
# 	usrchoices['Carex scoparia']=carexscoparia
# carexsquarrosa = st.number_input('Carex squarrosa', min_value=0, max_value=500, step=1)
# if carexsquarrosa:
# 	usrchoices['Carex squarrosa']=carexsquarrosa
# carexstipata = st.number_input('Carex stipata', min_value=0, max_value=500, step=1)
# if carexstipata:
# 	usrchoices['Carex stipata']=carexstipata
# carexstricta = st.number_input('Carex stricta', min_value=0, max_value=500, step=1)
# if carexstricta:
# 	usrchoices['Carex stricta']=carexstricta
# carexvulpinoidea = st.number_input('Carex vulpinoidea', min_value=0, max_value=500, step=1)
# if carexvulpinoidea:
# 	usrchoices['Carex vulpinoidea']=carexvulpinoidea
# centaureacyanus = st.number_input('Centaurea cyanus', min_value=0, max_value=500, step=1)
# if centaureacyanus:
# 	usrchoices['Centaurea cyanus']=centaureacyanus
# chamaecristafasciculata = st.number_input('Chamaecrista fasciculata', min_value=0, max_value=500, step=1)
# if chamaecristafasciculata:
# 	usrchoices['Chamaecrista fasciculata']=chamaecristafasciculata
# chamaecristanictitans = st.number_input('Chamaecrista nictitans', min_value=0, max_value=500, step=1)
# if chamaecristanictitans:
# 	usrchoices['Chamaecrista nictitans']=chamaecristanictitans
# chasmanthiumlatifolium = st.number_input('Chasmanthium latifolium', min_value=0, max_value=500, step=1)
# if chasmanthiumlatifolium:
# 	usrchoices['Chasmanthium latifolium']=chasmanthiumlatifolium
# chasmanthiumlaxum = st.number_input('Chasmanthium laxum', min_value=0, max_value=500, step=1)
# if chasmanthiumlaxum:
# 	usrchoices['Chasmanthium laxum']=chasmanthiumlaxum
# cheiranthusallionii = st.number_input('Cheiranthus allionii', min_value=0, max_value=500, step=1)
# if cheiranthusallionii:
# 	usrchoices['Cheiranthus allionii']=cheiranthusallionii
# cheloneglabra = st.number_input('Chelone glabra', min_value=0, max_value=500, step=1)
# if cheloneglabra:
# 	usrchoices['Chelone glabra']=cheloneglabra
# chrysanthemumcarinatum = st.number_input('Chrysanthemum carinatum', min_value=0, max_value=500, step=1)
# if chrysanthemumcarinatum:
# 	usrchoices['Chrysanthemum carinatum']=chrysanthemumcarinatum
# chrysanthemumleucanthemum = st.number_input('Chrysanthemum leucanthemum', min_value=0, max_value=500, step=1)
# if chrysanthemumleucanthemum:
# 	usrchoices['Chrysanthemum leucanthemum']=chrysanthemumleucanthemum
# chrysanthemummaximum = st.number_input('Chrysanthemum maximum', min_value=0, max_value=500, step=1)
# if chrysanthemummaximum:
# 	usrchoices['Chrysanthemum maximum']=chrysanthemummaximum
# cichoriumintybus = st.number_input('Cichorium intybus', min_value=0, max_value=500, step=1)
# if cichoriumintybus:
# 	usrchoices['Cichorium intybus']=cichoriumintybus
# cimicifugaracemosa = st.number_input('Cimicifuga racemosa', min_value=0, max_value=500, step=1)
# if cimicifugaracemosa:
# 	usrchoices['Cimicifuga racemosa']=cimicifugaracemosa
# cinnaarundinacea = st.number_input('Cinna arundinacea', min_value=0, max_value=500, step=1)
# if cinnaarundinacea:
# 	usrchoices['Cinna arundinacea']=cinnaarundinacea
# clarkiaelegans = st.number_input('Clarkia elegans', min_value=0, max_value=500, step=1)
# if clarkiaelegans:
# 	usrchoices['Clarkia elegans']=clarkiaelegans
# coreopsisbasalis = st.number_input('Coreopsis basalis', min_value=0, max_value=500, step=1)
# if coreopsisbasalis:
# 	usrchoices['Coreopsis basalis']=coreopsisbasalis
# coreopsisgrandiflora = st.number_input('Coreopsis grandiflora', min_value=0, max_value=500, step=1)
# if coreopsisgrandiflora:
# 	usrchoices['Coreopsis grandiflora']=coreopsisgrandiflora
# coreopsislanceolata = st.number_input('Coreopsis lanceolata', min_value=0, max_value=500, step=1)
# if coreopsislanceolata:
# 	usrchoices['Coreopsis lanceolata']=coreopsislanceolata
# coreopsisleavenworthii = st.number_input('Coreopsis leavenworthii', min_value=0, max_value=500, step=1)
# if coreopsisleavenworthii:
# 	usrchoices['Coreopsis leavenworthii']=coreopsisleavenworthii
# coreopsismajor = st.number_input('Coreopsis major', min_value=0, max_value=500, step=1)
# if coreopsismajor:
# 	usrchoices['Coreopsis major']=coreopsismajor
# coreopsistinctoria = st.number_input('Coreopsis tinctoria', min_value=0, max_value=500, step=1)
# if coreopsistinctoria:
# 	usrchoices['Coreopsis tinctoria']=coreopsistinctoria
# coreopsistripteris = st.number_input('Coreopsis tripteris', min_value=0, max_value=500, step=1)
# if coreopsistripteris:
# 	usrchoices['Coreopsis tripteris']=coreopsistripteris
# coreopsisverticillata = st.number_input('Coreopsis verticillata', min_value=0, max_value=500, step=1)
# if coreopsisverticillata:
# 	usrchoices['Coreopsis verticillata']=coreopsisverticillata
# cosmosbipinnatus = st.number_input('Cosmos bipinnatus', min_value=0, max_value=500, step=1)
# if cosmosbipinnatus:
# 	usrchoices['Cosmos bipinnatus']=cosmosbipinnatus
# cosmossulphureus = st.number_input('Cosmos sulphureus', min_value=0, max_value=500, step=1)
# if cosmossulphureus:
# 	usrchoices['Cosmos sulphureus']=cosmossulphureus
# crotoncapitatus = st.number_input('Croton capitatus', min_value=0, max_value=500, step=1)
# if crotoncapitatus:
# 	usrchoices['Croton capitatus']=crotoncapitatus
# dactylisglomerata = st.number_input('Dactylis glomerata', min_value=0, max_value=500, step=1)
# if dactylisglomerata:
# 	usrchoices['Dactylis glomerata']=dactylisglomerata
# daleacandida = st.number_input('Dalea candida', min_value=0, max_value=500, step=1)
# if daleacandida:
# 	usrchoices['Dalea candida']=daleacandida
# daleapurpurea = st.number_input('Dalea purpurea', min_value=0, max_value=500, step=1)
# if daleapurpurea:
# 	usrchoices['Dalea purpurea']=daleapurpurea
# daucuscarota = st.number_input('Daucus carota', min_value=0, max_value=500, step=1)
# if daucuscarota:
# 	usrchoices['Daucus carota']=daucuscarota
# delphiniumajacis = st.number_input('Delphinium ajacis', min_value=0, max_value=500, step=1)
# if delphiniumajacis:
# 	usrchoices['Delphinium ajacis']=delphiniumajacis
# desmanthusillinoensis = st.number_input('Desmanthus illinoensis', min_value=0, max_value=500, step=1)
# if desmanthusillinoensis:
# 	usrchoices['Desmanthus illinoensis']=desmanthusillinoensis
# desmodiumcanadense = st.number_input('Desmodium canadense', min_value=0, max_value=500, step=1)
# if desmodiumcanadense:
# 	usrchoices['Desmodium canadense']=desmodiumcanadense
# desmodiumglabellum = st.number_input('Desmodium glabellum', min_value=0, max_value=500, step=1)
# if desmodiumglabellum:
# 	usrchoices['Desmodium glabellum']=desmodiumglabellum
# desmodiumpaniculatum = st.number_input('Desmodium paniculatum', min_value=0, max_value=500, step=1)
# if desmodiumpaniculatum:
# 	usrchoices['Desmodium paniculatum']=desmodiumpaniculatum
# desmodiumtortuosum = st.number_input('Desmodium tortuosum', min_value=0, max_value=500, step=1)
# if desmodiumtortuosum:
# 	usrchoices['Desmodium tortuosum']=desmodiumtortuosum
# dianthusbarbatus = st.number_input('Dianthus barbatus', min_value=0, max_value=500, step=1)
# if dianthusbarbatus:
# 	usrchoices['Dianthus barbatus']=dianthusbarbatus
# dulichiumarundinaceum = st.number_input('Dulichium arundinaceum', min_value=0, max_value=500, step=1)
# if dulichiumarundinaceum:
# 	usrchoices['Dulichium arundinaceum']=dulichiumarundinaceum
# echinaceapallida = st.number_input('Echinacea pallida', min_value=0, max_value=500, step=1)
# if echinaceapallida:
# 	usrchoices['Echinacea pallida']=echinaceapallida
# echinaceapurpurea = st.number_input('Echinacea purpurea', min_value=0, max_value=500, step=1)
# if echinaceapurpurea:
# 	usrchoices['Echinacea purpurea']=echinaceapurpurea
# elephantopuselatus = st.number_input('Elephantopus elatus', min_value=0, max_value=500, step=1)
# if elephantopuselatus:
# 	usrchoices['Elephantopus elatus']=elephantopuselatus
# elymuscanadensis = st.number_input('Elymus canadensis', min_value=0, max_value=500, step=1)
# if elymuscanadensis:
# 	usrchoices['Elymus canadensis']=elymuscanadensis
# elymushystrix = st.number_input('Elymus hystrix', min_value=0, max_value=500, step=1)
# if elymushystrix:
# 	usrchoices['Elymus hystrix']=elymushystrix
# elymusriparius = st.number_input('Elymus riparius', min_value=0, max_value=500, step=1)
# if elymusriparius:
# 	usrchoices['Elymus riparius']=elymusriparius
# elymusvirginicus = st.number_input('Elymus virginicus', min_value=0, max_value=500, step=1)
# if elymusvirginicus:
# 	usrchoices['Elymus virginicus']=elymusvirginicus
# eragrostiscurvula = st.number_input('Eragrostis curvula', min_value=0, max_value=500, step=1)
# if eragrostiscurvula:
# 	usrchoices['Eragrostis curvula']=eragrostiscurvula
# eragrostiselliottii = st.number_input('Eragrostis elliottii', min_value=0, max_value=500, step=1)
# if eragrostiselliottii:
# 	usrchoices['Eragrostis elliottii']=eragrostiselliottii
# eragrostishirsuta = st.number_input('Eragrostis hirsuta', min_value=0, max_value=500, step=1)
# if eragrostishirsuta:
# 	usrchoices['Eragrostis hirsuta']=eragrostishirsuta
# eragrostisspectabilis = st.number_input('Eragrostis spectabilis', min_value=0, max_value=500, step=1)
# if eragrostisspectabilis:
# 	usrchoices['Eragrostis spectabilis']=eragrostisspectabilis
# eragrotistrichodes = st.number_input('Eragrotis trichodes', min_value=0, max_value=500, step=1)
# if eragrotistrichodes:
# 	usrchoices['Eragrotis trichodes']=eragrotistrichodes
# erianthuscontortus = st.number_input('Erianthus contortus', min_value=0, max_value=500, step=1)
# if erianthuscontortus:
# 	usrchoices['Erianthus contortus']=erianthuscontortus
# eriophorumvirginicum = st.number_input('Eriophorum virginicum', min_value=0, max_value=500, step=1)
# if eriophorumvirginicum:
# 	usrchoices['Eriophorum virginicum']=eriophorumvirginicum
# eryngiumaquaticumvaraquaticum = st.number_input('Eryngium aquaticum var. aquaticum', min_value=0, max_value=500, step=1)
# if eryngiumaquaticumvaraquaticum:
# 	usrchoices['Eryngium aquaticum var. aquaticum']=eryngiumaquaticumvaraquaticum
# eryngiumaquaticumvarravenelii = st.number_input('Eryngium aquaticum var. ravenelii', min_value=0, max_value=500, step=1)
# if eryngiumaquaticumvarravenelii:
# 	usrchoices['Eryngium aquaticum var. ravenelii']=eryngiumaquaticumvarravenelii
# eryngiumyuccifolium = st.number_input('Eryngium yuccifolium', min_value=0, max_value=500, step=1)
# if eryngiumyuccifolium:
# 	usrchoices['Eryngium yuccifolium']=eryngiumyuccifolium
# eschscholziacalifornica = st.number_input('Eschscholzia californica', min_value=0, max_value=500, step=1)
# if eschscholziacalifornica:
# 	usrchoices['Eschscholzia californica']=eschscholziacalifornica
# eupatoriumcoelestinum = st.number_input('Eupatorium coelestinum', min_value=0, max_value=500, step=1)
# if eupatoriumcoelestinum:
# 	usrchoices['Eupatorium coelestinum']=eupatoriumcoelestinum
# eupatoriumfistulosum = st.number_input('Eupatorium fistulosum', min_value=0, max_value=500, step=1)
# if eupatoriumfistulosum:
# 	usrchoices['Eupatorium fistulosum']=eupatoriumfistulosum
# eupatoriummaculatum = st.number_input('Eupatorium maculatum', min_value=0, max_value=500, step=1)
# if eupatoriummaculatum:
# 	usrchoices['Eupatorium maculatum']=eupatoriummaculatum
# eupatoriumperfoliatum = st.number_input('Eupatorium perfoliatum', min_value=0, max_value=500, step=1)
# if eupatoriumperfoliatum:
# 	usrchoices['Eupatorium perfoliatum']=eupatoriumperfoliatum
# eupatoriumpurpureum = st.number_input('Eupatorium purpureum', min_value=0, max_value=500, step=1)
# if eupatoriumpurpureum:
# 	usrchoices['Eupatorium purpureum']=eupatoriumpurpureum
# eupatoriumrugosum = st.number_input('Eupatorium rugosum', min_value=0, max_value=500, step=1)
# if eupatoriumrugosum:
# 	usrchoices['Eupatorium rugosum']=eupatoriumrugosum
# euphorbiacorollata = st.number_input('Euphorbia corollata', min_value=0, max_value=500, step=1)
# if euphorbiacorollata:
# 	usrchoices['Euphorbia corollata']=euphorbiacorollata
# euthamiacaroliniana = st.number_input('Euthamia caroliniana', min_value=0, max_value=500, step=1)
# if euthamiacaroliniana:
# 	usrchoices['Euthamia caroliniana']=euthamiacaroliniana
# euthamiagraminifolia = st.number_input('Euthamia graminifolia', min_value=0, max_value=500, step=1)
# if euthamiagraminifolia:
# 	usrchoices['Euthamia graminifolia']=euthamiagraminifolia
# festucaarundinacea = st.number_input('Festuca arundinacea', min_value=0, max_value=500, step=1)
# if festucaarundinacea:
# 	usrchoices['Festuca arundinacea']=festucaarundinacea
# festucaovinavarduriuscula = st.number_input('Festuca ovina var. duriuscula', min_value=0, max_value=500, step=1)
# if festucaovinavarduriuscula:
# 	usrchoices['Festuca ovina var. duriuscula']=festucaovinavarduriuscula
# festucaovinavarglauca = st.number_input('Festuca ovina var. glauca', min_value=0, max_value=500, step=1)
# if festucaovinavarglauca:
# 	usrchoices['Festuca ovina var. glauca']=festucaovinavarglauca
# festucaovina = st.number_input('Festuca ovina', min_value=0, max_value=500, step=1)
# if festucaovina:
# 	usrchoices['Festuca ovina']=festucaovina
# festucarubrasspcommutata = st.number_input('Festuca rubra ssp. commutata', min_value=0, max_value=500, step=1)
# if festucarubrasspcommutata:
# 	usrchoices['Festuca rubra ssp. commutata']=festucarubrasspcommutata
# festucarubra = st.number_input('Festuca rubra', min_value=0, max_value=500, step=1)
# if festucarubra:
# 	usrchoices['Festuca rubra']=festucarubra
# gaillardiaaristata = st.number_input('Gaillardia aristata', min_value=0, max_value=500, step=1)
# if gaillardiaaristata:
# 	usrchoices['Gaillardia aristata']=gaillardiaaristata
# gaillardiapulchella = st.number_input('Gaillardia pulchella', min_value=0, max_value=500, step=1)
# if gaillardiapulchella:
# 	usrchoices['Gaillardia pulchella']=gaillardiapulchella
# gaurabiennis = st.number_input('Gaura biennis', min_value=0, max_value=500, step=1)
# if gaurabiennis:
# 	usrchoices['Gaura biennis']=gaurabiennis
# gentianaclausa = st.number_input('Gentiana clausa', min_value=0, max_value=500, step=1)
# if gentianaclausa:
# 	usrchoices['Gentiana clausa']=gentianaclausa
# geumcanadense = st.number_input('Geum canadense', min_value=0, max_value=500, step=1)
# if geumcanadense:
# 	usrchoices['Geum canadense']=geumcanadense
# glyceriacanadensis = st.number_input('Glyceria canadensis', min_value=0, max_value=500, step=1)
# if glyceriacanadensis:
# 	usrchoices['Glyceria canadensis']=glyceriacanadensis
# glyceriagrandis = st.number_input('Glyceria grandis', min_value=0, max_value=500, step=1)
# if glyceriagrandis:
# 	usrchoices['Glyceria grandis']=glyceriagrandis
# glyceriaseptentrionalis = st.number_input('Glyceria septentrionalis', min_value=0, max_value=500, step=1)
# if glyceriaseptentrionalis:
# 	usrchoices['Glyceria septentrionalis']=glyceriaseptentrionalis
# glyceriastriata = st.number_input('Glyceria striata', min_value=0, max_value=500, step=1)
# if glyceriastriata:
# 	usrchoices['Glyceria striata']=glyceriastriata
# gypsophilaelegans = st.number_input('Gypsophila elegans', min_value=0, max_value=500, step=1)
# if gypsophilaelegans:
# 	usrchoices['Gypsophila elegans']=gypsophilaelegans
# heleniumautumnale = st.number_input('Helenium autumnale', min_value=0, max_value=500, step=1)
# if heleniumautumnale:
# 	usrchoices['Helenium autumnale']=heleniumautumnale
# heleniumflexuosum = st.number_input('Helenium flexuosum', min_value=0, max_value=500, step=1)
# if heleniumflexuosum:
# 	usrchoices['Helenium flexuosum']=heleniumflexuosum
# helianthusangustifolius = st.number_input('Helianthus angustifolius', min_value=0, max_value=500, step=1)
# if helianthusangustifolius:
# 	usrchoices['Helianthus angustifolius']=helianthusangustifolius
# helianthusannuus = st.number_input('Helianthus annuus', min_value=0, max_value=500, step=1)
# if helianthusannuus:
# 	usrchoices['Helianthus annuus']=helianthusannuus
# helianthusgiganteus = st.number_input('Helianthus giganteus', min_value=0, max_value=500, step=1)
# if helianthusgiganteus:
# 	usrchoices['Helianthus giganteus']=helianthusgiganteus
# helianthusmaximilianii = st.number_input('Helianthus maximilianii', min_value=0, max_value=500, step=1)
# if helianthusmaximilianii:
# 	usrchoices['Helianthus maximilianii']=helianthusmaximilianii
# helianthusoccidentalisvardowellianus = st.number_input('Helianthus occidentalis var. dowellianus', min_value=0, max_value=500, step=1)
# if helianthusoccidentalisvardowellianus:
# 	usrchoices['Helianthus occidentalis var. dowellianus']=helianthusoccidentalisvardowellianus
# helianthusradula = st.number_input('Helianthus radula', min_value=0, max_value=500, step=1)
# if helianthusradula:
# 	usrchoices['Helianthus radula']=helianthusradula
# heliopsishelianthoides = st.number_input('Heliopsis helianthoides', min_value=0, max_value=500, step=1)
# if heliopsishelianthoides:
# 	usrchoices['Heliopsis helianthoides']=heliopsishelianthoides
# hesperismatronalis = st.number_input('Hesperis matronalis', min_value=0, max_value=500, step=1)
# if hesperismatronalis:
# 	usrchoices['Hesperis matronalis']=hesperismatronalis
# hibiscusmoscheutos = st.number_input('Hibiscus moscheutos', min_value=0, max_value=500, step=1)
# if hibiscusmoscheutos:
# 	usrchoices['Hibiscus moscheutos']=hibiscusmoscheutos
# hordeumjubatum = st.number_input('Hordeum jubatum', min_value=0, max_value=500, step=1)
# if hordeumjubatum:
# 	usrchoices['Hordeum jubatum']=hordeumjubatum
# hypericumperforatum = st.number_input('Hypericum perforatum', min_value=0, max_value=500, step=1)
# if hypericumperforatum:
# 	usrchoices['Hypericum perforatum']=hypericumperforatum
# hypericumpunctatum = st.number_input('Hypericum punctatum', min_value=0, max_value=500, step=1)
# if hypericumpunctatum:
# 	usrchoices['Hypericum punctatum']=hypericumpunctatum
# hypericumpyramidatum = st.number_input('Hypericum pyramidatum', min_value=0, max_value=500, step=1)
# if hypericumpyramidatum:
# 	usrchoices['Hypericum pyramidatum']=hypericumpyramidatum
# irisversicolor = st.number_input('Iris versicolor', min_value=0, max_value=500, step=1)
# if irisversicolor:
# 	usrchoices['Iris versicolor']=irisversicolor
# irisvirginica = st.number_input('Iris virginica', min_value=0, max_value=500, step=1)
# if irisvirginica:
# 	usrchoices['Iris virginica']=irisvirginica
# juncuscanadensis = st.number_input('Juncus canadensis', min_value=0, max_value=500, step=1)
# if juncuscanadensis:
# 	usrchoices['Juncus canadensis']=juncuscanadensis
# juncuscoriaceus = st.number_input('Juncus coriaceus', min_value=0, max_value=500, step=1)
# if juncuscoriaceus:
# 	usrchoices['Juncus coriaceus']=juncuscoriaceus
# juncuseffusus = st.number_input('Juncus effusus', min_value=0, max_value=500, step=1)
# if juncuseffusus:
# 	usrchoices['Juncus effusus']=juncuseffusus
# juncustenuis = st.number_input('Juncus tenuis', min_value=0, max_value=500, step=1)
# if juncustenuis:
# 	usrchoices['Juncus tenuis']=juncustenuis
# juncustorreyi = st.number_input('Juncus torreyi', min_value=0, max_value=500, step=1)
# if juncustorreyi:
# 	usrchoices['Juncus torreyi']=juncustorreyi
# khuniaeupatorioides = st.number_input('Khunia eupatorioides', min_value=0, max_value=500, step=1)
# if khuniaeupatorioides:
# 	usrchoices['Khunia eupatorioides']=khuniaeupatorioides
# koeleriamacrantha = st.number_input('Koeleria macrantha', min_value=0, max_value=500, step=1)
# if koeleriamacrantha:
# 	usrchoices['Koeleria macrantha']=koeleriamacrantha
# kosteletzkyavirginica = st.number_input('Kosteletzkya virginica', min_value=0, max_value=500, step=1)
# if kosteletzkyavirginica:
# 	usrchoices['Kosteletzkya virginica']=kosteletzkyavirginica
# lathyrussylvestris = st.number_input('Lathyrus sylvestris', min_value=0, max_value=500, step=1)
# if lathyrussylvestris:
# 	usrchoices['Lathyrus sylvestris']=lathyrussylvestris
# lavateratrimestris = st.number_input('Lavatera trimestris', min_value=0, max_value=500, step=1)
# if lavateratrimestris:
# 	usrchoices['Lavatera trimestris']=lavateratrimestris
# leersiaoryzoides = st.number_input('Leersia oryzoides', min_value=0, max_value=500, step=1)
# if leersiaoryzoides:
# 	usrchoices['Leersia oryzoides']=leersiaoryzoides
# lespedezabicolor = st.number_input('Lespedeza bicolor', min_value=0, max_value=500, step=1)
# if lespedezabicolor:
# 	usrchoices['Lespedeza bicolor']=lespedezabicolor
# lespedezacapitata = st.number_input('Lespedeza capitata', min_value=0, max_value=500, step=1)
# if lespedezacapitata:
# 	usrchoices['Lespedeza capitata']=lespedezacapitata
# lespedezacuneata = st.number_input('Lespedeza cuneata', min_value=0, max_value=500, step=1)
# if lespedezacuneata:
# 	usrchoices['Lespedeza cuneata']=lespedezacuneata
# lespedezafrutescens = st.number_input('Lespedeza frutescens', min_value=0, max_value=500, step=1)
# if lespedezafrutescens:
# 	usrchoices['Lespedeza frutescens']=lespedezafrutescens
# lespedezastipulacea = st.number_input('Lespedeza stipulacea', min_value=0, max_value=500, step=1)
# if lespedezastipulacea:
# 	usrchoices['Lespedeza stipulacea']=lespedezastipulacea
# lespedezavirginica = st.number_input('Lespedeza virginica', min_value=0, max_value=500, step=1)
# if lespedezavirginica:
# 	usrchoices['Lespedeza virginica']=lespedezavirginica
# liatrisaspera = st.number_input('Liatris aspera', min_value=0, max_value=500, step=1)
# if liatrisaspera:
# 	usrchoices['Liatris aspera']=liatrisaspera
# liatriselegans = st.number_input('Liatris elegans', min_value=0, max_value=500, step=1)
# if liatriselegans:
# 	usrchoices['Liatris elegans']=liatriselegans
# liatrisgarberi = st.number_input('Liatris garberi', min_value=0, max_value=500, step=1)
# if liatrisgarberi:
# 	usrchoices['Liatris garberi']=liatrisgarberi
# liatrisgracilis = st.number_input('Liatris gracilis', min_value=0, max_value=500, step=1)
# if liatrisgracilis:
# 	usrchoices['Liatris gracilis']=liatrisgracilis
# liatrisgraminifolia = st.number_input('Liatris graminifolia', min_value=0, max_value=500, step=1)
# if liatrisgraminifolia:
# 	usrchoices['Liatris graminifolia']=liatrisgraminifolia
# liatrispycnostachya = st.number_input('Liatris pycnostachya', min_value=0, max_value=500, step=1)
# if liatrispycnostachya:
# 	usrchoices['Liatris pycnostachya']=liatrispycnostachya
# liatrisspicata = st.number_input('Liatris spicata', min_value=0, max_value=500, step=1)
# if liatrisspicata:
# 	usrchoices['Liatris spicata']=liatrisspicata
# liatrissquarrosa = st.number_input('Liatris squarrosa', min_value=0, max_value=500, step=1)
# if liatrissquarrosa:
# 	usrchoices['Liatris squarrosa']=liatrissquarrosa
# liatrissquarrulosa = st.number_input('Liatris squarrulosa', min_value=0, max_value=500, step=1)
# if liatrissquarrulosa:
# 	usrchoices['Liatris squarrulosa']=liatrissquarrulosa
# liliumsuperbum = st.number_input('Lilium superbum', min_value=0, max_value=500, step=1)
# if liliumsuperbum:
# 	usrchoices['Lilium superbum']=liliumsuperbum
# linariamaroccana = st.number_input('Linaria maroccana', min_value=0, max_value=500, step=1)
# if linariamaroccana:
# 	usrchoices['Linaria maroccana']=linariamaroccana
# linumgrandiflorumrubrum = st.number_input('Linum grandiflorum rubrum', min_value=0, max_value=500, step=1)
# if linumgrandiflorumrubrum:
# 	usrchoices['Linum grandiflorum rubrum']=linumgrandiflorumrubrum
# linumperenne = st.number_input('Linum perenne', min_value=0, max_value=500, step=1)
# if linumperenne:
# 	usrchoices['Linum perenne']=linumperenne
# linumusitatissimum = st.number_input('Linum usitatissimum', min_value=0, max_value=500, step=1)
# if linumusitatissimum:
# 	usrchoices['Linum usitatissimum']=linumusitatissimum
# lobeliacardinalis = st.number_input('Lobelia cardinalis', min_value=0, max_value=500, step=1)
# if lobeliacardinalis:
# 	usrchoices['Lobelia cardinalis']=lobeliacardinalis
# lobeliapuberula = st.number_input('Lobelia puberula', min_value=0, max_value=500, step=1)
# if lobeliapuberula:
# 	usrchoices['Lobelia puberula']=lobeliapuberula
# lobeliasiphilitica = st.number_input('Lobelia siphilitica', min_value=0, max_value=500, step=1)
# if lobeliasiphilitica:
# 	usrchoices['Lobelia siphilitica']=lobeliasiphilitica
# lobulariamaritima = st.number_input('Lobularia maritima', min_value=0, max_value=500, step=1)
# if lobulariamaritima:
# 	usrchoices['Lobularia maritima']=lobulariamaritima
# loliummultiflorum = st.number_input('Lolium multiflorum', min_value=0, max_value=500, step=1)
# if loliummultiflorum:
# 	usrchoices['Lolium multiflorum']=loliummultiflorum
# loliumperenne = st.number_input('Lolium perenne', min_value=0, max_value=500, step=1)
# if loliumperenne:
# 	usrchoices['Lolium perenne']=loliumperenne
# lotuscorniculatus = st.number_input('Lotus corniculatus', min_value=0, max_value=500, step=1)
# if lotuscorniculatus:
# 	usrchoices['Lotus corniculatus']=lotuscorniculatus
# ludwigiaalternifolia = st.number_input('Ludwigia alternifolia', min_value=0, max_value=500, step=1)
# if ludwigiaalternifolia:
# 	usrchoices['Ludwigia alternifolia']=ludwigiaalternifolia
# ludwigialinearis = st.number_input('Ludwigia linearis', min_value=0, max_value=500, step=1)
# if ludwigialinearis:
# 	usrchoices['Ludwigia linearis']=ludwigialinearis
# ludwigiamaritima = st.number_input('Ludwigia maritima', min_value=0, max_value=500, step=1)
# if ludwigiamaritima:
# 	usrchoices['Ludwigia maritima']=ludwigiamaritima
# lupinusperennis = st.number_input('Lupinus perennis', min_value=0, max_value=500, step=1)
# if lupinusperennis:
# 	usrchoices['Lupinus perennis']=lupinusperennis
# lupinuspolyphyllus = st.number_input('Lupinus polyphyllus', min_value=0, max_value=500, step=1)
# if lupinuspolyphyllus:
# 	usrchoices['Lupinus polyphyllus']=lupinuspolyphyllus
# lycopusamericanus = st.number_input('Lycopus americanus', min_value=0, max_value=500, step=1)
# if lycopusamericanus:
# 	usrchoices['Lycopus americanus']=lycopusamericanus
# melilotusofficinalis = st.number_input('Melilotus officinalis', min_value=0, max_value=500, step=1)
# if melilotusofficinalis:
# 	usrchoices['Melilotus officinalis']=melilotusofficinalis
# mimulusringens = st.number_input('Mimulus ringens', min_value=0, max_value=500, step=1)
# if mimulusringens:
# 	usrchoices['Mimulus ringens']=mimulusringens
# monardafistulosa = st.number_input('Monarda fistulosa', min_value=0, max_value=500, step=1)
# if monardafistulosa:
# 	usrchoices['Monarda fistulosa']=monardafistulosa
# monardamedia = st.number_input('Monarda media', min_value=0, max_value=500, step=1)
# if monardamedia:
# 	usrchoices['Monarda media']=monardamedia
# monardapunctata = st.number_input('Monarda punctata', min_value=0, max_value=500, step=1)
# if monardapunctata:
# 	usrchoices['Monarda punctata']=monardapunctata
# muhlenbergiacapillaris = st.number_input('Muhlenbergia capillaris', min_value=0, max_value=500, step=1)
# if muhlenbergiacapillaris:
# 	usrchoices['Muhlenbergia capillaris']=muhlenbergiacapillaris
# muhlenbergiaschreberi = st.number_input('Muhlenbergia schreberi', min_value=0, max_value=500, step=1)
# if muhlenbergiaschreberi:
# 	usrchoices['Muhlenbergia schreberi']=muhlenbergiaschreberi
# oenotherabiennis = st.number_input('Oenothera biennis', min_value=0, max_value=500, step=1)
# if oenotherabiennis:
# 	usrchoices['Oenothera biennis']=oenotherabiennis
# oenotheraspeciosa = st.number_input('Oenothera speciosa', min_value=0, max_value=500, step=1)
# if oenotheraspeciosa:
# 	usrchoices['Oenothera speciosa']=oenotheraspeciosa
# onocleasensibilis = st.number_input('Onoclea sensibilis', min_value=0, max_value=500, step=1)
# if onocleasensibilis:
# 	usrchoices['Onoclea sensibilis']=onocleasensibilis
# panicumamarum = st.number_input('Panicum amarum', min_value=0, max_value=500, step=1)
# if panicumamarum:
# 	usrchoices['Panicum amarum']=panicumamarum
# panicumanceps = st.number_input('Panicum anceps', min_value=0, max_value=500, step=1)
# if panicumanceps:
# 	usrchoices['Panicum anceps']=panicumanceps
# panicumclandestinum = st.number_input('Panicum clandestinum', min_value=0, max_value=500, step=1)
# if panicumclandestinum:
# 	usrchoices['Panicum clandestinum']=panicumclandestinum
# panicumdichotomiflorum = st.number_input('Panicum dichotomiflorum', min_value=0, max_value=500, step=1)
# if panicumdichotomiflorum:
# 	usrchoices['Panicum dichotomiflorum']=panicumdichotomiflorum
# panicumrigidulum = st.number_input('Panicum rigidulum', min_value=0, max_value=500, step=1)
# if panicumrigidulum:
# 	usrchoices['Panicum rigidulum']=panicumrigidulum
# panicumvirgatum = st.number_input('Panicum virgatum', min_value=0, max_value=500, step=1)
# if panicumvirgatum:
# 	usrchoices['Panicum virgatum']=panicumvirgatum
# papavernudicale = st.number_input('Papaver nudicale', min_value=0, max_value=500, step=1)
# if papavernudicale:
# 	usrchoices['Papaver nudicale']=papavernudicale
# papaverrhoeas = st.number_input('Papaver rhoeas', min_value=0, max_value=500, step=1)
# if papaverrhoeas:
# 	usrchoices['Papaver rhoeas']=papaverrhoeas
# partheniumintegrifolium = st.number_input('Parthenium integrifolium ', min_value=0, max_value=500, step=1)
# if partheniumintegrifolium:
# 	usrchoices['Parthenium integrifolium ']=partheniumintegrifolium
# peltandravirginica = st.number_input('Peltandra virginica', min_value=0, max_value=500, step=1)
# if peltandravirginica:
# 	usrchoices['Peltandra virginica']=peltandravirginica
# penstemonaustralis = st.number_input('Penstemon australis', min_value=0, max_value=500, step=1)
# if penstemonaustralis:
# 	usrchoices['Penstemon australis']=penstemonaustralis
# penstemondigitalis = st.number_input('Penstemon digitalis', min_value=0, max_value=500, step=1)
# if penstemondigitalis:
# 	usrchoices['Penstemon digitalis']=penstemondigitalis
# penstemonhirsutus = st.number_input('Penstemon hirsutus', min_value=0, max_value=500, step=1)
# if penstemonhirsutus:
# 	usrchoices['Penstemon hirsutus']=penstemonhirsutus
# penstemonlaevigatus = st.number_input('Penstemon laevigatus', min_value=0, max_value=500, step=1)
# if penstemonlaevigatus:
# 	usrchoices['Penstemon laevigatus']=penstemonlaevigatus
# penstemonmultiflorus = st.number_input('Penstemon multiflorus', min_value=0, max_value=500, step=1)
# if penstemonmultiflorus:
# 	usrchoices['Penstemon multiflorus']=penstemonmultiflorus
# penthorumsedoides = st.number_input('Penthorum sedoides', min_value=0, max_value=500, step=1)
# if penthorumsedoides:
# 	usrchoices['Penthorum sedoides']=penthorumsedoides
# phaceliacampanularia = st.number_input('Phacelia campanularia', min_value=0, max_value=500, step=1)
# if phaceliacampanularia:
# 	usrchoices['Phacelia campanularia']=phaceliacampanularia
# phalarisarundinacea = st.number_input('Phalaris arundinacea', min_value=0, max_value=500, step=1)
# if phalarisarundinacea:
# 	usrchoices['Phalaris arundinacea']=phalarisarundinacea
# phleumpratense = st.number_input('Phleum pratense', min_value=0, max_value=500, step=1)
# if phleumpratense:
# 	usrchoices['Phleum pratense']=phleumpratense
# poacompressa = st.number_input('Poa compressa', min_value=0, max_value=500, step=1)
# if poacompressa:
# 	usrchoices['Poa compressa']=poacompressa
# poapalustris = st.number_input('Poa palustris', min_value=0, max_value=500, step=1)
# if poapalustris:
# 	usrchoices['Poa palustris']=poapalustris
# poapratensis = st.number_input('Poa pratensis', min_value=0, max_value=500, step=1)
# if poapratensis:
# 	usrchoices['Poa pratensis']=poapratensis
# poatrivialis = st.number_input('Poa trivialis', min_value=0, max_value=500, step=1)
# if poatrivialis:
# 	usrchoices['Poa trivialis']=poatrivialis
# polygonumpensylvanicum = st.number_input('Polygonum pensylvanicum', min_value=0, max_value=500, step=1)
# if polygonumpensylvanicum:
# 	usrchoices['Polygonum pensylvanicum']=polygonumpensylvanicum
# polygonumsagittatum = st.number_input('Polygonum sagittatum', min_value=0, max_value=500, step=1)
# if polygonumsagittatum:
# 	usrchoices['Polygonum sagittatum']=polygonumsagittatum
# pontederiacordata = st.number_input('Pontederia cordata', min_value=0, max_value=500, step=1)
# if pontederiacordata:
# 	usrchoices['Pontederia cordata']=pontederiacordata
# puccinelliadistans = st.number_input('Puccinellia distans', min_value=0, max_value=500, step=1)
# if puccinelliadistans:
# 	usrchoices['Puccinellia distans']=puccinelliadistans
# puccinellianuttalliana = st.number_input('Puccinellia nuttalliana', min_value=0, max_value=500, step=1)
# if puccinellianuttalliana:
# 	usrchoices['Puccinellia nuttalliana']=puccinellianuttalliana
# pycnanthemumincanum = st.number_input('Pycnanthemum incanum', min_value=0, max_value=500, step=1)
# if pycnanthemumincanum:
# 	usrchoices['Pycnanthemum incanum']=pycnanthemumincanum
# pycnanthemummuticum = st.number_input('Pycnanthemum muticum', min_value=0, max_value=500, step=1)
# if pycnanthemummuticum:
# 	usrchoices['Pycnanthemum muticum']=pycnanthemummuticum
# pycnanthemumtenuifolium = st.number_input('Pycnanthemum tenuifolium', min_value=0, max_value=500, step=1)
# if pycnanthemumtenuifolium:
# 	usrchoices['Pycnanthemum tenuifolium']=pycnanthemumtenuifolium
# pycnanthemumvirginianum = st.number_input('Pycnanthemum virginianum', min_value=0, max_value=500, step=1)
# if pycnanthemumvirginianum:
# 	usrchoices['Pycnanthemum virginianum']=pycnanthemumvirginianum
# ratibidacolumnaris = st.number_input('Ratibida columnaris', min_value=0, max_value=500, step=1)
# if ratibidacolumnaris:
# 	usrchoices['Ratibida columnaris']=ratibidacolumnaris
# ratibidacolumnifera = st.number_input('Ratibida columnifera', min_value=0, max_value=500, step=1)
# if ratibidacolumnifera:
# 	usrchoices['Ratibida columnifera']=ratibidacolumnifera
# ratibidapinnata = st.number_input('Ratibida pinnata', min_value=0, max_value=500, step=1)
# if ratibidapinnata:
# 	usrchoices['Ratibida pinnata']=ratibidapinnata
# rhexiamariana = st.number_input('Rhexia mariana', min_value=0, max_value=500, step=1)
# if rhexiamariana:
# 	usrchoices['Rhexia mariana']=rhexiamariana
# rhexiavirginica = st.number_input('Rhexia virginica', min_value=0, max_value=500, step=1)
# if rhexiavirginica:
# 	usrchoices['Rhexia virginica']=rhexiavirginica
# rhynchosporaglobularis = st.number_input('Rhynchospora globularis', min_value=0, max_value=500, step=1)
# if rhynchosporaglobularis:
# 	usrchoices['Rhynchospora globularis']=rhynchosporaglobularis
# rudbeckiaamplexicaulis = st.number_input('Rudbeckia amplexicaulis', min_value=0, max_value=500, step=1)
# if rudbeckiaamplexicaulis:
# 	usrchoices['Rudbeckia amplexicaulis']=rudbeckiaamplexicaulis
# rudbeckiafulgida = st.number_input('Rudbeckia fulgida', min_value=0, max_value=500, step=1)
# if rudbeckiafulgida:
# 	usrchoices['Rudbeckia fulgida']=rudbeckiafulgida
# rudbeckiahirta = st.number_input('Rudbeckia hirta', min_value=0, max_value=500, step=1)
# if rudbeckiahirta:
# 	usrchoices['Rudbeckia hirta']=rudbeckiahirta
# rudbeckialaciniata = st.number_input('Rudbeckia laciniata', min_value=0, max_value=500, step=1)
# if rudbeckialaciniata:
# 	usrchoices['Rudbeckia laciniata']=rudbeckialaciniata
# rudbeckiamohrii = st.number_input('Rudbeckia mohrii', min_value=0, max_value=500, step=1)
# if rudbeckiamohrii:
# 	usrchoices['Rudbeckia mohrii']=rudbeckiamohrii
# rudbeckianitida = st.number_input('Rudbeckia nitida', min_value=0, max_value=500, step=1)
# if rudbeckianitida:
# 	usrchoices['Rudbeckia nitida']=rudbeckianitida
# rudbeckiasubtomentosa = st.number_input('Rudbeckia subtomentosa', min_value=0, max_value=500, step=1)
# if rudbeckiasubtomentosa:
# 	usrchoices['Rudbeckia subtomentosa']=rudbeckiasubtomentosa
# rudbeckiatriloba = st.number_input('Rudbeckia triloba', min_value=0, max_value=500, step=1)
# if rudbeckiatriloba:
# 	usrchoices['Rudbeckia triloba']=rudbeckiatriloba
# sagittarialatifolia = st.number_input('Sagittaria latifolia', min_value=0, max_value=500, step=1)
# if sagittarialatifolia:
# 	usrchoices['Sagittaria latifolia']=sagittarialatifolia
# saururuscernuus = st.number_input('Saururus cernuus', min_value=0, max_value=500, step=1)
# if saururuscernuus:
# 	usrchoices['Saururus cernuus']=saururuscernuus
# schizachyriumscoparium = st.number_input('Schizachyrium scoparium', min_value=0, max_value=500, step=1)
# if schizachyriumscoparium:
# 	usrchoices['Schizachyrium scoparium']=schizachyriumscoparium
# scirpusacutus = st.number_input('Scirpus acutus', min_value=0, max_value=500, step=1)
# if scirpusacutus:
# 	usrchoices['Scirpus acutus']=scirpusacutus
# scirpusatrovirens = st.number_input('Scirpus atrovirens', min_value=0, max_value=500, step=1)
# if scirpusatrovirens:
# 	usrchoices['Scirpus atrovirens']=scirpusatrovirens
# scirpuscyperinus = st.number_input('Scirpus cyperinus', min_value=0, max_value=500, step=1)
# if scirpuscyperinus:
# 	usrchoices['Scirpus cyperinus']=scirpuscyperinus
# scirpusexpansus = st.number_input('Scirpus expansus', min_value=0, max_value=500, step=1)
# if scirpusexpansus:
# 	usrchoices['Scirpus expansus']=scirpusexpansus
# scirpuspendulus = st.number_input('Scirpus pendulus', min_value=0, max_value=500, step=1)
# if scirpuspendulus:
# 	usrchoices['Scirpus pendulus']=scirpuspendulus
# scirpuspolyphyllus = st.number_input('Scirpus polyphyllus', min_value=0, max_value=500, step=1)
# if scirpuspolyphyllus:
# 	usrchoices['Scirpus polyphyllus']=scirpuspolyphyllus
# scirpusrobustus = st.number_input('Scirpus robustus', min_value=0, max_value=500, step=1)
# if scirpusrobustus:
# 	usrchoices['Scirpus robustus']=scirpusrobustus
# scirpusvalidus = st.number_input('Scirpus validus', min_value=0, max_value=500, step=1)
# if scirpusvalidus:
# 	usrchoices['Scirpus validus']=scirpusvalidus
# scutellariaincana = st.number_input('Scutellaria incana', min_value=0, max_value=500, step=1)
# if scutellariaincana:
# 	usrchoices['Scutellaria incana']=scutellariaincana
# sennahebecarpa = st.number_input('Senna hebecarpa', min_value=0, max_value=500, step=1)
# if sennahebecarpa:
# 	usrchoices['Senna hebecarpa']=sennahebecarpa
# sennamarilandica = st.number_input('Senna marilandica', min_value=0, max_value=500, step=1)
# if sennamarilandica:
# 	usrchoices['Senna marilandica']=sennamarilandica
# silenearmeria = st.number_input('Silene armeria', min_value=0, max_value=500, step=1)
# if silenearmeria:
# 	usrchoices['Silene armeria']=silenearmeria
# silphiumasteriscusvarangustatum = st.number_input('Silphium asteriscus var. angustatum', min_value=0, max_value=500, step=1)
# if silphiumasteriscusvarangustatum:
# 	usrchoices['Silphium asteriscus var. angustatum']=silphiumasteriscusvarangustatum
# silphiumasteriscusvarlaevicaule = st.number_input('Silphium asteriscus var. laevicaule', min_value=0, max_value=500, step=1)
# if silphiumasteriscusvarlaevicaule:
# 	usrchoices['Silphium asteriscus var. laevicaule']=silphiumasteriscusvarlaevicaule
# silphiumintegrifolium = st.number_input('Silphium integrifolium', min_value=0, max_value=500, step=1)
# if silphiumintegrifolium:
# 	usrchoices['Silphium integrifolium']=silphiumintegrifolium
# silphiumlaciniatum = st.number_input('Silphium laciniatum', min_value=0, max_value=500, step=1)
# if silphiumlaciniatum:
# 	usrchoices['Silphium laciniatum']=silphiumlaciniatum
# silphiumperfoliatum = st.number_input('Silphium perfoliatum', min_value=0, max_value=500, step=1)
# if silphiumperfoliatum:
# 	usrchoices['Silphium perfoliatum']=silphiumperfoliatum
# silphiumterebinthaceum = st.number_input('Silphium terebinthaceum', min_value=0, max_value=500, step=1)
# if silphiumterebinthaceum:
# 	usrchoices['Silphium terebinthaceum']=silphiumterebinthaceum
# silphiumtrifoliatum = st.number_input('Silphium trifoliatum', min_value=0, max_value=500, step=1)
# if silphiumtrifoliatum:
# 	usrchoices['Silphium trifoliatum']=silphiumtrifoliatum
# sisyrinchiumangustifolium = st.number_input('Sisyrinchium angustifolium', min_value=0, max_value=500, step=1)
# if sisyrinchiumangustifolium:
# 	usrchoices['Sisyrinchium angustifolium']=sisyrinchiumangustifolium
# solidagobicolor = st.number_input('Solidago bicolor', min_value=0, max_value=500, step=1)
# if solidagobicolor:
# 	usrchoices['Solidago bicolor']=solidagobicolor
# solidagocaesia = st.number_input('Solidago caesia', min_value=0, max_value=500, step=1)
# if solidagocaesia:
# 	usrchoices['Solidago caesia']=solidagocaesia
# solidagocanadensis = st.number_input('Solidago canadensis', min_value=0, max_value=500, step=1)
# if solidagocanadensis:
# 	usrchoices['Solidago canadensis']=solidagocanadensis
# solidagofistulosa = st.number_input('Solidago fistulosa', min_value=0, max_value=500, step=1)
# if solidagofistulosa:
# 	usrchoices['Solidago fistulosa']=solidagofistulosa
# solidagoflexicaulis = st.number_input('Solidago flexicaulis', min_value=0, max_value=500, step=1)
# if solidagoflexicaulis:
# 	usrchoices['Solidago flexicaulis']=solidagoflexicaulis
# solidagojuncea = st.number_input('Solidago juncea', min_value=0, max_value=500, step=1)
# if solidagojuncea:
# 	usrchoices['Solidago juncea']=solidagojuncea
# solidagonemoralis = st.number_input('Solidago nemoralis', min_value=0, max_value=500, step=1)
# if solidagonemoralis:
# 	usrchoices['Solidago nemoralis']=solidagonemoralis
# solidagoodora = st.number_input('Solidago odora', min_value=0, max_value=500, step=1)
# if solidagoodora:
# 	usrchoices['Solidago odora']=solidagoodora
# solidagopatula = st.number_input('Solidago patula', min_value=0, max_value=500, step=1)
# if solidagopatula:
# 	usrchoices['Solidago patula']=solidagopatula
# solidagoriddellii = st.number_input('Solidago riddellii', min_value=0, max_value=500, step=1)
# if solidagoriddellii:
# 	usrchoices['Solidago riddellii']=solidagoriddellii
# solidagorigida = st.number_input('Solidago rigida', min_value=0, max_value=500, step=1)
# if solidagorigida:
# 	usrchoices['Solidago rigida']=solidagorigida
# solidagorugosa = st.number_input('Solidago rugosa', min_value=0, max_value=500, step=1)
# if solidagorugosa:
# 	usrchoices['Solidago rugosa']=solidagorugosa
# solidagosempervirens = st.number_input('Solidago sempervirens', min_value=0, max_value=500, step=1)
# if solidagosempervirens:
# 	usrchoices['Solidago sempervirens']=solidagosempervirens
# solidagospeciosa = st.number_input('Solidago speciosa', min_value=0, max_value=500, step=1)
# if solidagospeciosa:
# 	usrchoices['Solidago speciosa']=solidagospeciosa
# solidagostricta = st.number_input('Solidago stricta', min_value=0, max_value=500, step=1)
# if solidagostricta:
# 	usrchoices['Solidago stricta']=solidagostricta
# sorghastrumelliotti = st.number_input('Sorghastrum elliotti', min_value=0, max_value=500, step=1)
# if sorghastrumelliotti:
# 	usrchoices['Sorghastrum elliotti']=sorghastrumelliotti
# sorghastrumnutans = st.number_input('Sorghastrum nutans', min_value=0, max_value=500, step=1)
# if sorghastrumnutans:
# 	usrchoices['Sorghastrum nutans']=sorghastrumnutans
# sorghastrumsecundum = st.number_input('Sorghastrum secundum', min_value=0, max_value=500, step=1)
# if sorghastrumsecundum:
# 	usrchoices['Sorghastrum secundum']=sorghastrumsecundum
# sparganiumamericanum = st.number_input('Sparganium americanum', min_value=0, max_value=500, step=1)
# if sparganiumamericanum:
# 	usrchoices['Sparganium americanum']=sparganiumamericanum
# sparganiumeurycarpum = st.number_input('Sparganium eurycarpum', min_value=0, max_value=500, step=1)
# if sparganiumeurycarpum:
# 	usrchoices['Sparganium eurycarpum']=sparganiumeurycarpum
# spartinapectinata = st.number_input('Spartina pectinata', min_value=0, max_value=500, step=1)
# if spartinapectinata:
# 	usrchoices['Spartina pectinata']=spartinapectinata
# sporobolusasper = st.number_input('Sporobolus asper', min_value=0, max_value=500, step=1)
# if sporobolusasper:
# 	usrchoices['Sporobolus asper']=sporobolusasper
# sporoboluscryptandrus = st.number_input('Sporobolus cryptandrus', min_value=0, max_value=500, step=1)
# if sporoboluscryptandrus:
# 	usrchoices['Sporobolus cryptandrus']=sporoboluscryptandrus
# sporobolusheterolepis = st.number_input('Sporobolus heterolepis', min_value=0, max_value=500, step=1)
# if sporobolusheterolepis:
# 	usrchoices['Sporobolus heterolepis']=sporobolusheterolepis
# sporobolusjunceus = st.number_input('Sporobolus junceus', min_value=0, max_value=500, step=1)
# if sporobolusjunceus:
# 	usrchoices['Sporobolus junceus']=sporobolusjunceus
# thalictrumpubescens = st.number_input('Thalictrum pubescens', min_value=0, max_value=500, step=1)
# if thalictrumpubescens:
# 	usrchoices['Thalictrum pubescens']=thalictrumpubescens
# tradescantiaohiensis = st.number_input('Tradescantia ohiensis', min_value=0, max_value=500, step=1)
# if tradescantiaohiensis:
# 	usrchoices['Tradescantia ohiensis']=tradescantiaohiensis
# tradescantiasubaspera = st.number_input('Tradescantia subaspera', min_value=0, max_value=500, step=1)
# if tradescantiasubaspera:
# 	usrchoices['Tradescantia subaspera']=tradescantiasubaspera
# tradescantiavirginiana = st.number_input('Tradescantia virginiana', min_value=0, max_value=500, step=1)
# if tradescantiavirginiana:
# 	usrchoices['Tradescantia virginiana']=tradescantiavirginiana
# tridensflavus = st.number_input('Tridens flavus', min_value=0, max_value=500, step=1)
# if tridensflavus:
# 	usrchoices['Tridens flavus']=tridensflavus
# trifoliumhybridum = st.number_input('Trifolium hybridum', min_value=0, max_value=500, step=1)
# if trifoliumhybridum:
# 	usrchoices['Trifolium hybridum']=trifoliumhybridum
# trifoliumincarnatum = st.number_input('Trifolium incarnatum', min_value=0, max_value=500, step=1)
# if trifoliumincarnatum:
# 	usrchoices['Trifolium incarnatum']=trifoliumincarnatum
# trifoliumpratense = st.number_input('Trifolium pratense', min_value=0, max_value=500, step=1)
# if trifoliumpratense:
# 	usrchoices['Trifolium pratense']=trifoliumpratense
# trifoliumrepens = st.number_input('Trifolium repens', min_value=0, max_value=500, step=1)
# if trifoliumrepens:
# 	usrchoices['Trifolium repens']=trifoliumrepens
# tripsacumdactyloides = st.number_input('Tripsacum dactyloides', min_value=0, max_value=500, step=1)
# if tripsacumdactyloides:
# 	usrchoices['Tripsacum dactyloides']=tripsacumdactyloides
# typhaangustifolia = st.number_input('Typha angustifolia', min_value=0, max_value=500, step=1)
# if typhaangustifolia:
# 	usrchoices['Typha angustifolia']=typhaangustifolia
# typhalatifolia = st.number_input('Typha latifolia', min_value=0, max_value=500, step=1)
# if typhalatifolia:
# 	usrchoices['Typha latifolia']=typhalatifolia
# veratrumviride = st.number_input('Veratrum viride', min_value=0, max_value=500, step=1)
# if veratrumviride:
# 	usrchoices['Veratrum viride']=veratrumviride
# verbenahastata = st.number_input('Verbena hastata', min_value=0, max_value=500, step=1)
# if verbenahastata:
# 	usrchoices['Verbena hastata']=verbenahastata
# verbenastricta = st.number_input('Verbena stricta', min_value=0, max_value=500, step=1)
# if verbenastricta:
# 	usrchoices['Verbena stricta']=verbenastricta
# verbenaurticifolia = st.number_input('Verbena urticifolia', min_value=0, max_value=500, step=1)
# if verbenaurticifolia:
# 	usrchoices['Verbena urticifolia']=verbenaurticifolia
# verbesinaalternifolia = st.number_input('Verbesina alternifolia', min_value=0, max_value=500, step=1)
# if verbesinaalternifolia:
# 	usrchoices['Verbesina alternifolia']=verbesinaalternifolia
# vernoniaacaulis = st.number_input('Vernonia acaulis', min_value=0, max_value=500, step=1)
# if vernoniaacaulis:
# 	usrchoices['Vernonia acaulis']=vernoniaacaulis
# vernoniaangustifolia = st.number_input('Vernonia angustifolia', min_value=0, max_value=500, step=1)
# if vernoniaangustifolia:
# 	usrchoices['Vernonia angustifolia']=vernoniaangustifolia
# vernoniagigantea = st.number_input('Vernonia gigantea', min_value=0, max_value=500, step=1)
# if vernoniagigantea:
# 	usrchoices['Vernonia gigantea']=vernoniagigantea
# vernonianoveboracensis = st.number_input('Vernonia noveboracensis', min_value=0, max_value=500, step=1)
# if vernonianoveboracensis:
# 	usrchoices['Vernonia noveboracensis']=vernonianoveboracensis
# veronicastrumvirginicum = st.number_input('Veronicastrum virginicum', min_value=0, max_value=500, step=1)
# if veronicastrumvirginicum:
# 	usrchoices['Veronicastrum virginicum']=veronicastrumvirginicum
# violacornuta = st.number_input('Viola cornuta', min_value=0, max_value=500, step=1)
# if violacornuta:
# 	usrchoices['Viola cornuta']=violacornuta
# ziziaaurea = st.number_input('Zizia aurea', min_value=0, max_value=500, step=1)
# if ziziaaurea:
# 	usrchoices['Zizia aurea']=ziziaaurea
# zizaniaaquatica = st.number_input('Zizania aquatica', min_value=0, max_value=500, step=1)
# if zizaniaaquatica:
# 	usrchoices['Zizania aquatica']=zizaniaaquatica

##make a new data frame with the dictionary of user choices and relevant data from SEEDS
DATA = pd.read_csv("SEEDS.csv").set_index("species")

usrchoicesdf=pd.DataFrame.from_dict(usrchoices, orient="index", columns=["plants_per_meter"])

st.write("You chose:", usrchoicesdf)

usrseed =DATA.loc[usrchoicesdf.index,]

seeddf=pd.concat([usrseed, usrchoicesdf], axis=1)


#These calculation takes us from the inputted values to values that can be purchased. 
#plants per square meter * square meters to acres conversion / germination rate * seeds per pound = 
#how many seeds per pound you need per acre to get the number of plants desired per square meter
seeddf["pounds_per_acre"]=seeddf["plants_per_meter"] / seeddf["seeds_per_lb"] * 4046.86 / seeddf["germ_rate"]
            
#It's customary to include percent by weight as well to help scale the mix up or down from an acre
seeddf["percent_by_weight"] = seeddf.pounds_per_acre / seeddf.pounds_per_acre.sum()
            
if seeddf.fall.sum() > 0:
	st.write("Some species on your list require cold stratification. Fall planting recommended to reduce dormancy and improve establishment.")


if seeddf.loc[seeddf['forb']==1].plants_per_meter.sum()/seeddf.plants_per_meter.sum() > .60:
    st.write("Consider adding more grasses or sedges to improve weed suppression and prevent erosion, especially if your site is sloped.")

seeddf.seeds_per_meter= seeddf.plants_per_meter / seeddf.germ_rate 
if seeddf.seeds_per_meter.sum()<400.0: 
    st.write("Consider increasing number of plants for better weed suppression and erosion control.")    

if seeddf.seeds_per_meter.sum()>1200.0:
	st.write("Consider decreasing desired density of plants to maintain diversity.")
#This will show the output table on streamlit using st.write
purchaselist=seeddf.filter([ "common_name", "seeds_per_lb", "pounds_per_acre", "percent_by_weight"], axis=1)

st.write("### Purchase List", purchaselist.sort_index())
st.write("The seeding rate of your mix is {} pounds per acre".format(seeddf.pounds_per_acre.sum()))
st.write("Seed with an equal volume of bulking agent, such as kitty litter, and an appropiate nurse crop from the list below.")

st.write("Here is an example of the graphing from your sample data:")


#this for loop generates the plotting data
choices=pd.DataFrame((seeddf.index.values, seeddf["common_name"], seeddf["plants_per_meter"]), index=None).T.rename(columns={0: "species", 1: "common_name", 2: "plants_per_meter"})
#choices["plants_per_meter"]=int(choices["plants_per_meter"])

species = []
common_name= []
x = []
y = []
for index, row in choices.iterrows():
    for i in range (1, row['plants_per_meter']):
        species.append(row["species"])
        common_name.append(row["common_name"])
        x.append(random.uniform(0, 1))
        y.append(random.uniform(0, 1))
metercalc = pd.DataFrame((species, common_name, x, y), index=None).T.rename(columns={0:"species", 1:"common_name", 2:"x", 3:"y"})

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
