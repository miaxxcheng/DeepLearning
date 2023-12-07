# import os
# import llama_index
# os.environ["OPENAI_API_KEY"] = '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'

# from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

# documents = SimpleDirectoryReader('data').load_data()
# index = GPTVectorStoreIndex(documents)

# # save to disk
# index.save_to_disk('index_training.json')

import openai

openai.api_key = "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"

# openai.Completion.create(
#     model="curie",
#     prompt="Which Thai Restaurant has the best Pad Thai")

# with open("finetune_training_data_prepared.jsonl") as file:
#     response = openai.File.create(
#         file=file,
#         purpose='fine-tune'
#     )

#export OPENAI_API_KEY="<OPENAI_API_KEY>"
#openai tools fine_tunes.prepare_data -f finetune_training_data.csv
#openai api fine_tunes.create -t "finetune_training_data_prepared.jsonl"
#openai api fine_tunes.list
#file-Qj9Sre2GExUhoUH0Xz2wYLJv



#Using File ID

# fileid="file-Qj9Sre2GExUhoUH0Xz2wYLJv"
# model_name = "gpt-3.5-turbo"

# response = openai.FineTuningJob.create(
#     training_file = file_id,
#     model=model_name
# )

# job_id = response['id']
# print("Fine Tuning Successful")

#ft-F3gUJNNralHL1yxRmJxwlNT8
#  "data": [
#     {
#       "created_at": 1701981353,
#       "fine_tuned_model": "curie:ft-yonsei-univ-2023-12-07-20-58-51",
#       "hyperparams": {
#         "batch_size": 1,
#         "learning_rate_multiplier": 0.1,
#         "n_epochs": 4,
#         "prompt_loss_weight": 0.01
#       },
#       "id": "ft-F3gUJNNralHL1yxRmJxwlNT8",
#       "model": "curie",
#       "object": "fine-tune",
#       "organization_id": "org-AAFUUne3gJJIY9UWsuotWTKi",
#       "result_files": [
#         {
#           "bytes": 21548,
#           "created_at": 1701982732,
#           "filename": "compiled_results.csv",
#           "id": "file-IcYde25WmBsZU5F9xAYMuSIf",
#           "object": "file",
#           "purpose": "fine-tune-results",
#           "status": "processed",
#           "status_details": null
#         }
#       ],
#       "status": "succeeded",
#       "training_files": [
#         {
#           "bytes": 23985,
#           "created_at": 1701981353,
#           "filename": "finetune_training_data_prepared.jsonl",
#           "id": "file-Qj9Sre2GExUhoUH0Xz2wYLJv",
#           "object": "file",
#           "purpose": "fine-tune",
#           "status": "processed",
#           "status_details": null
#         }
#       ],
#       "updated_at": 1701982732,
#       "validation_files": []
#     }
#   ],
#   "next_starting_after": null,
#   "object": "list"

#ft-yonsei-univ-2023-12-07-20-58-51



