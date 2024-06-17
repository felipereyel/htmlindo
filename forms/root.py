import uuid
import flask_sock


form_template = """
    <form id="aform" ws-send class="text-white text-center px-4 py-2 bg-blue-600 border border-slate-600 rounded shadow-md flex flex-col justify-center items-center">
        
        <label for="field">{label}</label>

        <input type="text" name="field" class="text-slate-600 w-96 mt-4 px-2 py-1 border border-slate-600 rounded shadow-md" placeholder="{placeholder}"></input>

        <input type="submit" class="mt-2 px-4 py-1 bg-blue-600 hover:bg-sky-100 hover:text-sky-900 text-white rounded shadow-md" value="send"></input>

    </form>
"""

end_template = """
    <div id="pform" class="text-white text-center flex flex-col justify-center items-center h-full">

        <p class="h-10 px-4 py-2 bg-green-600 border border-slate-600 rounded shadow-md ">{message}</p>

    </div>
"""


def run(ws: flask_sock.Server):
    # wait for start
    ws.receive()

    for _ in range(3):
        label = f"Name ({uuid.uuid4()})"
        form = form_template.format(label=label, placeholder="Enter your name")
        ws.send(form)
        ws.receive()

    ws.send(end_template.format(message="Thank you for your time!"))
