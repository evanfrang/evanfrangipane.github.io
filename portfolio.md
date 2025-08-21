---
layout: page 
title: Portfolio
permalink: /portfolio/
order: 2
---

## Streaming Fraud Sandbox

I created a sandbox for synthetic user music streaming data to test what methods are useful for finding bots and fraudulent users.

I am also using [Streamlit](https://streamingfraud.streamlit.app/) to host a dashboard for playing around with the dataset.

The code can be found at [https://github.com/evanfrang/streaming_fraud_analysis](https://github.com/evanfrang/streaming_fraud_analysis).

Here is a screenshot from the online dashboard:

![sl](/img/streamlit.png){: width="1000" }

## GenAI for Creating Abstracts

Fine-tuned tiny llama on title, category, and abstract data to generate novel abstracts.
Take a look at the code at [https://github.com/evanfrang/abstract_generator](https://github.com/evanfrang/abstract_generator).

```
--- Abstract Generation ---
Category: astro-ph
Title: Measuring the Expansion of the Universe and Testing de Sitter

Generated Abstract:
We present a method to measure the Hubble parameter from the expansion rate
of the universe in a de Sitter space. Our method is based on the relation
between the Hubble parameter and the deceleration parameter in a de Sitter
space, which is a generalization of the equation of state parameter. This
relation is used to calculate the deceleration parameter from the Hubble
parameter. We show that the deceleration parameter can be measured from the
Hubble parameter with an accuracy of 1% for a de Sitter universe. We also
present a method to measure the expansion rate of the universe using the
deceleration parameter.
```

## arxbot: LLM trained on Physics Abstracts

Small chatbot using physics abstracts as context via RAG pipeline.
Take a look at the code at [https://github.com/evanfrang/arxbot](https://github.com/evanfrang/arxbot).

```
Ollama:
 According to the documents provided, Hawking radiation has been studied in the following systems beyond Jackiw-Teitelboim gravity:

1. Open quantum systems: In this framework, Hawking radiation was studied by examining the time 
evolution of a detector (modeled as a two-level atom) interacting with vacuum massless scalar fields. 
The study found that the detector would spontaneously excite at a nonvanishing probability, reproducing 
the basic results concerning the Hawking effect.
2. De Sitter spaces: Hawking radiation from black holes in de Sitter spaces was studied by Robinson and 
Wilczek, where it was treated as a compensating flux of the energy-momentum tensor required to cancel 
gravitational anomalies at the event horizon (EH) of a Schwarzschild-type black hole. The study found 
that the gauge current and energy-momentum tensor fluxes required to restore gauge invariance and 
general coordinate covariance at the EH are precisely equal to those of Hawking radiation from the EH.
3. Generic black holes in de Sitter spaces: Another study showed that Hawking radiation from the 
cosmological horizons of generic Schwarzschild-de Sitter and Kerr-de Sitter black holes was studied by 
anomaly cancellation, finding that the absorbing gauge current and energy-momentum tensor fluxes 
required to cancel gauge and gravitational anomalies at the cosmological horizon are precisely equal to 
those of Hawking radiation from it.

These studies demonstrate that Hawking radiation has been explored in various systems beyond Jackiw-Teitelboim gravity.
```

## End-to-End arXiv Abstract Classification

[Live model for classifiying abstracts!](https://arxiv-classifier.onrender.com/)

Find the code and a write-up at [https://github.com/evanfrang/arxiv_classifier](https://github.com/evanfrang/arxiv_classifier). 

Here is the confusion matrix for the live Logistic Regression model.

![cm](/img/lrconfusion.png){: width="1000" }


## Weather Forecasting with ML

I used Gaussian Processes and Prophet to do time series forecsting on daily temperatures.
The code can be found at [https://github.com/evanfrang/weather_bayes/](https://github.com/evanfrang/weather_bayes/).

On top we have Gaussian Process and on bottom we have Prophet forecasting temperatures.

![cm](/img/gp.png){: width="1000" }
![cm](/img/prophet.png){: width="1000" }


## Model Comparison for Credit Card Fraud Classification

Find the code and a write-up at [https://github.com/evanfrang/fraud_detection](https://github.com/evanfrang/fraud_detection). 

![auc](/img/auc.png){: width="1000" }

## Happiness Trends Worldwide: A Comparative View 2015 - 2024

Tableau dashboard for happiness changes from 2015 to 2024 from the World Happiness Report.
The dashboard can be found [here](https://public.tableau.com/app/profile/evan.frangipane/viz/WorldHappinessChanges2015to2024/finaldashboard).

![whr](/img/WHR_map.JPG){: width="1000" }

This map shows the percent change of happiness from before 2020 to 2020 and beyond.
The global change was a 2.7% increase in happiness.

The datasets can be found on my [github](https://github.com/evanfrang/world_happiness).
