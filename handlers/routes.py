from flask import render_template, request
import modules.dfa_before_minimization as dfa_bm


def configure_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        if (request.method == "POST"):
            state = request.form["state"]
            alphabet = request.form["alphabet"]
            delta = request.form["delta"]
            initial = request.form["initial"]
            final = request.form["final"]

            # Before minimization
            edgeBM = dfa_bm.get_edge(delta)
            edgeLabelBM = dfa_bm.get_edge_label(delta)
            stateBM = dfa_bm.get_state(state)
            alphabetBM = dfa_bm.get_alphabet(alphabet)
            initialBM = dfa_bm.get_initial(initial)
            finalBM = dfa_bm.get_final(final)
            transitionTableBM = dfa_bm.get_transition_table(
                state, alphabet, delta)
            detailedDescriptionBM = dfa_bm.get_detailed_description(delta)
            templateData = {
                "isSubmit": True,
                # Before Minimization
                "edgeBM": edgeBM,
                "edgeLabelBM": edgeLabelBM,
                "stateBM": stateBM,
                "alphabetBM": alphabetBM,
                "initialBM": initialBM,
                "finalBM": finalBM,
                "transitionTableBM": transitionTableBM,
                "detailedDescriptionBM": detailedDescriptionBM,
                # After Minimization
            }
            return render_template("index.html", **templateData)
        else:
            return render_template("index.html")
