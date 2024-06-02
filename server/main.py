import argparse, json, uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

global PATH
global resources

parser = argparse.ArgumentParser(description="Run FastAPI server with JSON file")
parser.add_argument("file_path", type=str, help="Path to the JSON file")
args = parser.parse_args()
PATH = args.file_path
resources = json.load(open(PATH, "r"))

def update_resources_file():
	with open("./data.json", "w") as f:
		json.dump(resources, f, indent=4)

def add_entry_to_resource(request_json: dict, resource):
	try:
		"""
		TODO: add check to ensure id is unique, maybe username too
		"""
		fields = resources[resource][0].keys()
		data = {}
		for key in request_json.keys():
			if key not in fields:
				continue
			data[key] = request_json[key]
		resources[resource].append(data)

		update_resources_file(resources)

		return data
	except:
		raise HTTPException(status_code=500, detail="Internal Server Error")

def delete_entry_from_resource(id: str, resource: str):
    updated_resource_data = [entry for entry in resources[resource] if str(entry['id']) != str(id)]
    resources[resource] = updated_resource_data
    update_resources_file()
    return updated_resource_data

app = FastAPI()

@app.get('/{resource}')
async def get_resource(resource: str):
	if resource not in resources.keys():
		raise HTTPException(status_code=404, detail="Not Found")
	return resources[resource]

@app.post('/{resource}')
async def add_resources(resource: str, request: Request):
	if resource not in resources.keys():
		raise HTTPException(status_code=404, detail="Not Found")

	request_json = await request.json()
	data = add_entry_to_resource(request_json, resource)

	return JSONResponse(content=data, status_code=201)

@app.delete('/{resource}/{id}')
async def delete_resource(resource: str, id: str):
	if resource not in resources.keys():
		raise HTTPException(status_code=404, detail="Not Found")
	delete_entry_from_resource(id, resource)
	return JSONResponse(content={'success' : True}, status_code=200)

uvicorn.run(app,host="0.0.0.0", port=8000)