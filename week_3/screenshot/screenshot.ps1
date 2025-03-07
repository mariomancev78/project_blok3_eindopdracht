$Path = "C:\ScreenCapture"
If (!(Test-Path $Path)) {
    New-Item -ItemType Directory -Force -Path $Path
}
Add-Type -AssemblyName System.Windows.Forms
$screen = [Windows.Forms.SystemInformation]::VirtualScreen
$image = New-Object System.Drawing.Bitmap($screen.Width, $screen.Height)
$graphic = [System.Drawing.Graphics]::FromImage($image)
$point = New-Object System.Drawing.Point(0, 0)
$graphic.CopyFromScreen($point, $point, $image.Size)
$cursorBounds = New-Object System.Drawing.Rectangle([System.Windows.Forms.Cursor]::Position, [System.Windows.Forms.Cursor]::Current.Size)
[System.Windows.Forms.Cursors]::Default.Draw($graphic, $cursorBounds)
$screen_file = "$Path\screenshot.png"
$image.Save($screen_file, [System.Drawing.Imaging.ImageFormat]::Png)
$graphic.Dispose()
$image.Dispose()
Write-Output "Screenshot opgeslagen als: $screen_file"

