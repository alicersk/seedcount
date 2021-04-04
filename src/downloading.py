#!/usr/bin/env python

import streamlit as st
import pandas as pd


def download_link(data, stats):
    """
    Generates a link to download the Seed Mix Specification
    """
    object_to_download=stats.purchaselist.reset_index().rename(columns={'index':'latin_name'})
    download_filename='seedcount_purchaselist.csv'

    object_to_download = object_to_download.to_csv(index=False)

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}"><input type="button" value="Download Seed Mix as CSV"></a>'

