from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import uvicorn

async def homepage(request):
    return JSONResponse({'hello': 'world'})
async def about(request):
    return JSONResponse({'about': 'here you can meet the team'})
async def contact(request):
    return JSONResponse({'contact': 'how you could contact us'})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/about', about),
    Route('/contact', contact)
])

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
