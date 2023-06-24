import fiftyone as fo
import multiprocessing
import os


FIFTYONE_URI = os.getenv("FIFTYONE_URI", '0.0.0.0')
FIFTYONE_PORT = int(os.getenv("FIFTYONE_PORT", 5151))
JUPYTER_PORT= int(os.getenv("JUPYTER_PORT", 8889))
JUPYTER_FILE_PATH= str(os.getenv('JUPYTER_FILE_PATH'))


def run_fiftyone():
    datasets = fo.list_datasets()
    # print(datasets)
    if len(datasets) == 0 or datasets == None:
        session =  fo.launch_app(address=FIFTYONE_URI, port=FIFTYONE_PORT)
    else:
        dataset = fo.load_dataset(datasets[-1])
        session = fo.launch_app(dataset=dataset, address=FIFTYONE_URI, port=FIFTYONE_PORT)
    # print(session)
    session.wait()


def run_jupyterlab():
    jupyter_cli_command = f"jupyter-lab {JUPYTER_FILE_PATH} --port {JUPYTER_PORT} --allow-root --ip 0.0.0.0 --LabApp.token=''"
    # print(JUPYTER_FILE_PATH)
    if JUPYTER_FILE_PATH == "None" or JUPYTER_FILE_PATH == None:
        jupyter_cli_command = f"jupyter-lab --port {JUPYTER_PORT} --allow-root --ip 0.0.0.0 --LabApp.token=''"
    os.system(jupyter_cli_command)

if __name__ == "__main__":
    os.chdir(os.getcwd())
    task_1 = multiprocessing.Process(target=run_fiftyone)
    task_2 = multiprocessing.Process(target=run_jupyterlab)
    task_1.start()
    task_2.start()
    task_1.join()
    task_2.join()
   