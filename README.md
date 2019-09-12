# Boulder Fire Department - Incident Response 2015-2018

<src="folium_maps/folium_header.png">

## Table of Contents

1. [Overview](#overview)
2. [Data](#data)
3. [First Glance](#first-glance)
4. [When are incidents occurring?](#when-are-incidents-occurring?)
5. [What now?](#what-now?)


## Overview

Fire departments respond around the clock to a variety of incidents. This EDA primarily sought to quantify the the type of incidents the Boulder Fire Department (BFD) commonly respond to. This study also looked into the location of incidents, as well as investigated the timing of incidents over many different intervals to attempt to infer some information about when, where, and what the BFD are responding to.

## Data

The data was obtained directly from the Boulder government site [here](https://bouldercolorado.gov/open-data/boulder-fire-response-times/). The data was generally in good condition, consisting largely of information regarding incident location (latitude, longitude), multiple measures of response time, as well as general information regarding what the BFD was responding too. There were multiple columns with as many NaNs or zeros as actual data

For this study, data concerning ambulance responses, data from 2019, as well as any rows of information not containing latitude and longitude data for the sight of the incident, were not investigated.

## First Glance

Over the course of the four years investigated, the BFD responded to nearly 51.5 thousand incidents, which broke down nearly equally by year.

<src="images/Incidents_per_Year.png">

Of those incidents, the vast majority were responses to Emergency Medical Service (EMS) calls.

<src="images/Average_Incidents_per_Program_Area.png">

When the incidents were viewed by month, an interesting pattern appeared.

<src="images/Incidents_per_Month_Averaged.png">

## When are incidents occurring?

## What now?

I was curious what was causing that spike from August-October, and wanted to confirm what I was seeing.

<src="images/kde_plot_DoW_Year.png">

With this kernel density estimation (KDE) figure, I was able to confirm that the August-October are the months of the year that BFD tends to get the most calls. So what are those incidents that are inflating those months and where are they occurring?



