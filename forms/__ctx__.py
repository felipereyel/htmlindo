import json
import flask_sock

form_read_template = """
    <form id="aform" ws-send class="text-white text-center px-4 py-2 bg-blue-600 border border-slate-600 rounded shadow-md flex flex-col justify-center items-center">
        
        <label for="field">{label}</label>

        <input type="text" name="field" class="text-slate-600 w-96 mt-4 px-2 py-1 border border-slate-600 rounded shadow-md" placeholder="{placeholder}"></input>

        <input type="submit" class="mt-2 px-4 py-1 bg-blue-600 hover:bg-sky-100 hover:text-sky-900 text-white rounded shadow-md" value="send"></input>

    </form>
"""

form_display_template = """
    <form id="aform" ws-send class="text-white text-center px-4 py-2 bg-blue-600 border border-slate-600 rounded shadow-md flex flex-col justify-center items-center">
        
        <p>{message}</p>

        <input type="submit" class="mt-2 px-4 py-1 bg-blue-600 hover:bg-sky-100 hover:text-sky-900 text-white rounded shadow-md" value="send"></input>
        
    </form>
"""


end_template = """
    <div id="pform" class="text-white text-center flex flex-col justify-center items-center h-full">

        <p class="h-10 px-4 py-2 bg-green-600 border border-slate-600 rounded shadow-md ">{message}</p>

    </div>
"""


class Context:
    ws: flask_sock.Server

    def __init__(self, ws: flask_sock.Server):
        self.ws = ws

    def __enter__(self):
        self.ws.receive()
        return self

    def __exit__(self, *args):
        self.ws.send(end_template.format(message="Thank you for your time!"))

    def _rcv(self):
        return json.loads(self.ws.receive())

    def _send(self, message: str):
        self.ws.send(message)

    def read(self, label: str, placeholder: str = ""):
        form = form_read_template.format(label=label, placeholder=placeholder)
        self._send(form)

        data = self._rcv()
        return data["field"]

    def display(self, message: str):
        form = form_display_template.format(message=message)
        self._send(form)

        self._rcv()
