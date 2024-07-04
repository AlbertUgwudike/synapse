from subprocess import run
import os
import pandas as pd
import numpy as np

DATA_DIR = "./data"
CP_EXEC = "/Applications/CellProfiler.app/Contents/MacOS/cp"
OUT_DIR = "./output"

def main():
    all_files = os.listdir(DATA_DIR)

    log("Looking for pipeline file ...")
    pipeline_files = list(filter(lambda fn: fn.endswith(".cppipe"), all_files))

    if (len(pipeline_files) != 1): 
        panic("There should be one .cppipe file in the 'data/' folder")
    
    pipeline_file = f"{DATA_DIR}/{pipeline_files[0]}"

    log(f"Discovered pipeline file: {pipeline_file}")
    log(f"Looking for image files ...")

    image_files = pipeline_files = list(filter(lambda fn: fn.endswith(".tif"), all_files))

    log(f"Discovered {len(image_files)} image files!")
    log("Running CellProfiler Batch ...")

    run([CP_EXEC, "-c", "-r", "-p", pipeline_file, "-o", "./output", "-i", DATA_DIR])

    log(f"Batch Completed!")
    log(f"Organising Data ...")

    vgat_selector = "Intensity_IntegratedIntensity_vgat"
    geph_selector = "Intensity_IntegratedIntensity_gephyrin"

    vgat_df = process_data(f"{DATA_DIR}/inh test set/denemeVGATSpots.csv", vgat_selector)
    vgat_df.to_csv(f"{OUT_DIR}/vgat.csv")

    geph_df = process_data(f"{DATA_DIR}/inh test set/denemeGephyrinSpots.csv", geph_selector)
    geph_df.to_csv(f"{OUT_DIR}/geph.csv")

    log(f"Finito")



def process_data(fname, col):
    cols = ["FileName_multiple", "AreaShape_Area", col]
    df = pd.read_csv(fname)[cols]
    agg_a = pd.NamedAgg(column="AreaShape_Area", aggfunc=lambda x: np.mean(x))
    agg_b = pd.NamedAgg(column=col, aggfunc=lambda x: np.mean(x))
    agg_c = pd.NamedAgg(column=col, aggfunc='count')
    return df.groupby("FileName_multiple").agg(Count = agg_c, Area = agg_a, Intensity = agg_b)

def panic(message):
    print(f"Error: {message}\n")
    exit()

def log(message): print(f"\n### SYNAPSE: {message} \n")

if __name__ == "__main__": main()