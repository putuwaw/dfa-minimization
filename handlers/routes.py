from flask import render_template, request
import modules.dfa_before_minimization as dfa_bm
import modules.dfa_minimization as dfa_min


def configure_routes(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route("/aplikasi", methods=["GET", "POST"])
    def aplikasi():
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

            # After minimization
            edgeMin = dfa_min.table_filling_method(
                state, alphabet, delta, initial, final, 1)
            edgeLabelMin = dfa_min.table_filling_method(
                state, alphabet, delta, initial, final, 2)
            stateMin = dfa_min.table_filling_method(
                state, alphabet, delta, initial, final, 3)
            alphabetMin = dfa_min.table_filling_method(
                state, alphabet, delta, initial, final, 4)
            initialMin = dfa_min.table_filling_method(
                state, alphabet, delta, initial, final, 5)
            finalMin = dfa_min.table_filling_method(
                state, alphabet, delta, initial, final, 6)
            transitionTableMin = dfa_min.table_filling_method(
                state, alphabet, delta, initial, final, 7)
            detailedDescriptionMin = dfa_min.table_filling_method(
                state, alphabet, delta, initial, final, 8)

            templateData = {
                "isSubmit": True,
                # Before minimization
                "edgeBM": edgeBM,
                "edgeLabelBM": edgeLabelBM,
                "stateBM": stateBM,
                "alphabetBM": alphabetBM,
                "initialBM": initialBM,
                "finalBM": finalBM,
                "transitionTableBM": transitionTableBM,
                "detailedDescriptionBM": detailedDescriptionBM,

                # After minimization
                "edgeMin": edgeMin,
                "edgeLabelMin": edgeLabelMin,
                "stateMin": stateMin,
                "alphabetMin": alphabetMin,
                "initialMin": initialMin,
                "finalMin": finalMin,
                "transitionTableMin": transitionTableMin,
                "detailedDescriptionMin": detailedDescriptionMin,
            }
            return render_template("app.html", **templateData)
        else:
            return render_template("app.html")
