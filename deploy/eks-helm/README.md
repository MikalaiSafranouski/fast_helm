### Helm needs to be downloaded and installed in your local machine.
Helm is a packager for Kubernetes that bundles related manifest files and packages
them into a single logical deployment unit: a Chart.



#### Reusing Statements Between Templates

Use `_helpers.tpl` to define reusable statements.
Create the _helpers.tpl file in the templates directory with the following content:
```
{{- define "fast-helm.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name}}
{{- end }}
```

Then replace the template placeholders shown in previous snippets with a call to the
podman.selectorLabels helper statement using the include keyword:
```
# Source: Deployment.yaml
spec:
    replicas: {{ .Values.replicaCount }}
    selector:
        matchLabels:
            {{- include "fast-helm.selectorLabels" . | nindent 6 }}
    template:
        metadata:
            labels:
                {{- include "fast-helm.selectorLabels" . | nindent 8 }}
        spec:
            containers:
```

    
If you want to update the selector labels, the only change you need to do is an update
to the _helpers.tpl file:
```
{{- define "pacman.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name}}
app.kubernetes.io/version: {{ .Chart.AppVersion}}
{{- end }}
```

Although it’s common to use __helpers.tpl as the filename to define
functions, you can name any file starting with __, and Helm will
read the functions too.


#### Updating a Container Image in Helm


Deploy version 1.0.0 of the application:
`$ helm install fast-helm .`

You can check revision number by running the following command:

`$ helm history fast-helm`


```angular2html
REVISION       UPDATED                         STATUS          CHART           APP VERSION     DESCRIPTION     
1               Tue Jan 16 11:48:50 2024        deployed        fast-helm-0.1.0 latest          Install complete
```

To update the version, open `values.yaml` and update the `image.tag` field to the newer
container image tag:

```angular2html
image:
  repository: safronovskiy/fast-messenger-service
  tag: "latest" -> "1.0.0"                              # update tag
  pullPolicy: Always
  servicePort: 80
  containerPort: 8000

replicaCount: 1
securityContext: {}    
```
Then update the appVersion field of the Chart.yaml file:

```angular2html
apiVersion: v2
name: fast-helm
description: A Helm chart for fast-helm-service

type: application

version: 0.1.0
appVersion: "1.0.0"                            # update
```
After these changes, upgrade the deployment by running the following command:

`$ helm upgrade fast-helm .`

Not only you can install or upgrade a version with Helm, but you can also roll back to
a previous revision.
In the terminal window, run the following command:

`$ helm rollback fast-helm 1`
(where `1`  is a revision number)



#### Triggering a Rolling Update Automatically

Use the sha256sum template function to generate a change on the deployment file.

Let’s use the sha256sum function to calculate an SHA-256 value of the configmap.yaml
file content and set it as a pod annotation, which effectively triggers a rolling update
as the pod definition has changed:
```
# Deployment.yaml

spec:
    replicas: {{ .Values.replicaCount }}
    selector:
        matchLabels:
            app.kubernetes.io/name: {{ .Chart.Name}}
    template:
        metadata:
            labels:
                app.kubernetes.io/name: {{ .Chart.Name}}
            annotations:
                checksum/config: {{ include (print $.Template.BasePath "/configmap.yaml") . | sha256sum }}
```




