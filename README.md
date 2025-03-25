[![OpenSSF Scorecard](htt‌ps://api.securityscorecards.dev/projects/github.com/{RobertReed1412}/{IntegrationFinal}/badge)](htt‌ps://securityscorecards.dev/viewer/?uri=github.com/{RobertReed1412}/{IntegrationFina})

- name: "Upload artifact"
  uses: actions/upload-artifact@v4
  with:
    name: SARIF file
    path: results.sarif
    retention-days: 5
