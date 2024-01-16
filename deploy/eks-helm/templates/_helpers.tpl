{{- define "fast-helm.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name}}
{{- end }}
