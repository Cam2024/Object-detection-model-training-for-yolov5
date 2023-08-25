import onnx

onnx_path = 'best.onnx'
onnx_model = onnx.load(onnx_path)
onnx.checker.check_model(onnx_model)
print("成功")