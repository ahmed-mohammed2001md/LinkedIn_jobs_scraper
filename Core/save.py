
import pandas as pd
import os
import Core.configure as config
class Save:

    def csv(data):
        pass

    def excel(data):
        print(data)
        # check if the folder is exists if not create one
        if not os.path.exists(f'{os.getcwd()}/{config.OUTPUTS_DIR}'):
            os.mkdir(f'{os.getcwd()}/{config.OUTPUTS_DIR}')

        # saving file dir
        file_path = f'{os.getcwd()}/{config.OUTPUTS_DIR}/{config.OUTPUT_FILE}.xlsx'

        # get the existing file if there
        try:
            existing_df = pd.read_excel(file_path)
        except FileNotFoundError:
            existing_df = pd.DataFrame()

        # Create SINGLE-ROW DataFrame from dictionary
        new_df = pd.DataFrame([data])  # ← Critical fix: Wrap data in list to make single row

        # Concatenate properly (ignore_index prevents duplication)
        combined_df = pd.concat([existing_df, new_df], ignore_index=True)

        # Write ONCE with full replacement (no append mode)
        combined_df.to_excel(file_path, index=False, sheet_name='Sheet1')
