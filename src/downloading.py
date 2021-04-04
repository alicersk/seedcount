#!/usr/bin/env python

import base64
import streamlit as st
import pandas as pd


def download_link(data, stats):
    """
    Generates a link to download the Seed Mix Specification as a csv
    """
    object_to_download=stats.purchaselist.reset_index().rename(columns={'index':'latin_name'})
    download_filename='seedcount_purchaselist.csv'

    object_to_download = object_to_download.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}"><input type="button" value="Download Seed Mix as CSV"></a>'

