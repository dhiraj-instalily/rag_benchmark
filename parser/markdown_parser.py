from dotenv import load_dotenv
import os
load_dotenv()
import joblib
from llama_parse import LlamaParse



def load_or_parse_data(list_file_path, output_file):
    if os.path.exists(output_file):
        # Load the parsed data from the file
        parsed_data = joblib.load(output_file)
    else:
        parser = LlamaParse(api_key=os.getenv('LLAMA_CLOUD_API_KEY'),
                            result_type="markdown",
                            verbose=True,
                            num_workers=5)
        llama_parse_documents = parser.load_data(list_file_path)

        print(f"Saving the parse results in {output_file} ..........")
        joblib.dump(llama_parse_documents, output_file)

        parsed_data = llama_parse_documents

    return parsed_data



#run parser
# list_file_path = ["data/hayward_1.pdf", "data/hayward_2.pdf", "data/hayward_3.pdf", "data/hayward_4.pdf", "data/hayward_5.pdf"]
# output_file = "output/hayward.pkl"
# test = load_or_parse_data(list_file_path, output_file)

