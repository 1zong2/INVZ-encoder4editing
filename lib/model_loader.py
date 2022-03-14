import numpy as np
import torch

def CreateModel(gpu, args):

    from your_model.model import YourModel
    from your_model.options import TrainOptions
    args = TrainOptions().parse()
    model = YourModel(args, gpu)
    args.isMaster = gpu == 0
    model.RandomGenerator = np.random.RandomState(42)
    model.initialize_models()
    model.set_dataset()

    if args.use_mGPU:
        model.set_multi_GPU()

    model.set_data_iterator()
    model.set_validation()
    model.set_optimizers()
    step = model.load_checkpoint()
    model.set_loss_collector()

    if args.isMaster:
        print(f'model {args.model_id} has created')
        
    return model, args, step