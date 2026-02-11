# Arwen

## About

**Arwen DCA** is designed to help clinicians aggregate diagnostic criteria based on the structure found in the DSM-5-TR.

> [!CAUTION]
> This is **not** a diagnostic tool and should not be used as such. Clinicians should always use their own judgement and verify that criteria and codes are correct.

Clincians can select all diagnostic criteria that apply to their patient/client and the tool will output a list of criteria met formatted in a way that can be easily copied into an EHR or note (including systems which parse criteria to :sparkles: automagically* :sparkles: create a note)

The tool does **not store any data** that is submitted and **does not allow the input of any PHI**. When a user refreshes a page or navigates away, all data is irrevocably lost.

This project is open source and available on [GitHub](https://github.com/hermaplusplus/Arwen). It is provided under the [MIT License](https://github.com/hermaplusplus/Arwen/blob/main/LICENSE). Contributions, issue reports, feedback, and suggestions are welcome.

<sub>Why is the tool called 'Arwen'? I watched Lord of the Rings recently. That's it.</sub>

<sub>* Automagically, meaning using a Large Language Model.</sub>

## Development

Arwen uses [uv](https://docs.astral.sh/uv/) as a package manager and [Docker Compose](https://docs.docker.com/compose/) for containerisation. To run the project, make sure you have these installed, as well as Python 3.11+.

To activate the virtual environment, run the appropriate (for your system) script under `./.venv/Scripts/`. 

To run the project during development, run `streamlit run main.py`.

To deploy the project in production, run `./start.sh`.
