$items = Get-ChildItem "R:\hw5\train" -Filter *.tar

foreach ($item in $items)
{
    $file = Get-Item $item.FullName
    $newLoc = $item.DirectoryName + "\" + $item.BaseName
    $newFile = $newLoc + "\" + $item.Name

    New-Item -Path $item.DirectoryName -Name $item.BaseName -ItemType "directory"

    Move-Item -Path $item.FullName -Destination $newFile

    cd $newLoc

    tar -xf $newFile

    Remove-Item $newFile
}