from setfit import SetFitModel

# Download from Hub and run inference
model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")
# Run inference
preds = model(["i loved the spiderman movie!", "pineapple on pizza is the worst 🤮", "It is not okkk"])
print(preds)