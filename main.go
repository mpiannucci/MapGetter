package MapGetter

import (
	"html/template"
	"net/http"
)

var index = template.Must(template.ParseFiles(
	"templates/base.html",
	"templates/index.html",
	"templates/map_form.html",
))

func init() {
	http.HandleFunc("/", root)
}

func root(w http.ResponseWriter, r *http.Request) {
	if err := index.Execute(w, nil); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}
