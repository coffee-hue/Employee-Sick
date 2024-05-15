"""Main loop start for the employees GraphQL API"""
import asyncio
import logging
from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart
from strawberry.quart.views import GraphQLView
from strawberry import Schema
from src.api.schemas import emlopyees

class employee_api:
    
    """
    employee_api class:
    
    start:

    run:
        
    """
    
    def __init__(self):
        logging.debug("Initialise employee API (graphql)")
        self.app = Quart("Employees sick API")
        
        self.query = "hello"
        
        self.schema = Schema(query=self.query)
        
        self.app.add_url_rule("/v1/employees",
                              view_func=GraphQLView.as_view("graphql_view", self.schema, False))
        
        self.hyper_config = Config()
        self.hyper_config.bind = ["127.0.0.1:8000"]
        self.hyper_config.use_reloader = True
        
        async def run(self):
            """Running the employee api(graphql)"""
            logging.debug("graphql run API")
            await serve(self.app, self.hyper_config, shutdown_trigger=lambda: asyncio.Future())

        def _cleanup(self, _f) -> None:
            """Cleaning up the employee api(graphql)"""
            logging.debug("Cleanup employee API (graphql)")
            
        def start(self, loop: asyncio.AbstractEventLoop) -> None:
            """starting up the employee api(graphql)"""
            logging.debug("Start graphql API")
            future = asyncio.ensure_future(self.run(), loop=loop)
            future.add_done_callback(self._cleanup)
        

def dev():
    
    app = Quart("Name")
    query = emlopyees.Query

    schema = Schema(query=query)

    app.add_url_rule("/v1/graphql",
            view_func=GraphQLView.as_view("graphql_view", schema))
    hyper_config = Config()
    hyper_config.bind = ["127.0.0.1:8000"]
    hyper_config.use_reloader = True
    loop = asyncio.get_event_loop()
    api_dev_ask = loop.create_task(serve(app, hyper_config, shutdown_trigger=lambda: asyncio.Future()))
    api_groups = asyncio.gather(api_dev_ask)
    loop.run_until_complete(api_groups)
    