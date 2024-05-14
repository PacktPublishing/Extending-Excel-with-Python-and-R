Sub MultiplyByRandom()
    Dim rng As Range
    Dim cell As Range
    
    ' Set the range to the desired range on Sheet2
    Set rng = Sheets("Sheet2").Range("C3:C13")
    
    ' Loop through each cell in the range
    For Each cell In rng
        ' Multiply the cell value by RAND() and store the result in the adjacent cell
        cell.Offset(0, 1).Value = cell.Value * Rnd()
    Next cell
End Sub