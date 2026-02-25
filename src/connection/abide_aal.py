import os

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import matplotlib.pyplot as plt
from nilearn import datasets, plotting
from nilearn.connectome import ConnectivityMeasure
from nilearn.maskers import NiftiLabelsMasker

# directory for output
os.makedirs("out/figures/abide/aal", exist_ok=True)

print("--- downloading single data from ABIDE... ---")

# fetching a single subject's preprocessed functional data from the ABIDE dataset
dataset = datasets.fetch_abide_pcp(n_subjects=1, pipeline='cpac', band_pass_filtering=True)

# loading the AAL atlas for parcellation
atlas = datasets.fetch_atlas_aal()
labels = atlas.labels

# extracting time series from the functional data using the AAL atlas
masker = NiftiLabelsMasker(
    labels_img=atlas.maps, 
    standardize='zscore_sample', # type: ignore
    memory='nilearn_cache', 
    verbose=5
)
time_series = masker.fit_transform(dataset.func_preproc[0])

# computing the correlation matrix from the extracted time series
correlation_measure = ConnectivityMeasure(
    kind='correlation', 
    standardize='zscore_sample'   # type: ignore
)
correlation_matrix = correlation_measure.fit_transform([time_series])[0]

print("--- plotting correlation matrix... ---")

# Slice labels to match matrix size
cleaned_labels = labels[:correlation_matrix.shape[0]]

# Use a context manager to temporarily shrink the font size for this plot only
import matplotlib
with matplotlib.rc_context({'font.size': 6}):
    display = plotting.plot_matrix(
        correlation_matrix, 
        labels=cleaned_labels,
        colorbar=True, 
        vmax=1, 
        vmin=-1,
        reorder='average' # type: ignore
    )

subject_id = str(dataset.phenotypic['SUB_ID'].iloc[0])
output_path = f"out/figures/abide/aal/connection_check_{subject_id}.png"
plt.savefig(output_path, bbox_inches='tight')

print(f"SUCCESS! Output saved to {output_path}")