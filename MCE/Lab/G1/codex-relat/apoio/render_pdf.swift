import Foundation
import PDFKit
import AppKit
let args = CommandLine.arguments
let pdf = PDFDocument(url: URL(fileURLWithPath: args[1]))!
let dest = args[2]
try! FileManager.default.createDirectory(atPath: dest, withIntermediateDirectories: true)
for i in 0..<pdf.pageCount {
 let page = pdf.page(at:i)!
 let img = page.thumbnail(of:NSSize(width:900,height:1273),for:.mediaBox)
 let rep = NSBitmapImageRep(data:img.tiffRepresentation!)!
 try! rep.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:"\(dest)/pagina_\(i+1).png"))
}
print(pdf.pageCount)
