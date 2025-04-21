from ts.torch_handler.base_handler import BaseHandler
import torch
import json

class StockPredictionHandler(BaseHandler):
    def initialize(self, context):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model_path = context.system_properties.get("model_dir") + "/model.pt"
        self.model = torch.load(model_path, map_location=self.device)
        self.model.eval()

    def preprocess(self, data):
        raw = data[0]['body']
        if isinstance(raw, (bytes, bytearray)):
            raw = raw.decode('utf-8')
        features = json.loads(raw)['data']
        tensor = torch.tensor(features, dtype=torch.float32).unsqueeze(0).to(self.device)
        return tensor

    def inference(self, model_input):
        with torch.no_grad():
            return self.model(model_input)

    def postprocess(self, inference_output):
        return inference_output.cpu().numpy().tolist()
