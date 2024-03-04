Sub MakeCurlRequestAndInsertImage()
    ' Define the curl command
    Dim curlCommand As String
    curlCommand = "curl -X GET ""http://127.0.0.1:6855/plot?.mean=0"" -H ""accept: image/png"" -o " & Environ("TEMP") & "\temp_image.png"

    ' Run the curl command using Shell
    Shell "cmd /c " & curlCommand, vbHide

    ' Create a new worksheet or refer to an existing one (Sheet1)
    Dim ws As Worksheet
    Set ws = ActiveWorkbook.Worksheets("Sheet1")

    ' Clear previous content in Sheet1
    ws.Cells.Clear

    ' Insert the image into the worksheet
    ws.Pictures.Insert(Environ("TEMP") & "\temp_image.png").Select
End Sub
