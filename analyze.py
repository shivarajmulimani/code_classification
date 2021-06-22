import lizard
import pandas as pd
import os
import argparse

def main(files_dir, path_to_save):

    # list all files
    # you can also filter files format extension here
    files = os.listdir(files_dir)

    # iterate over files
    for file in files:

        # lets declare variables to save results
        cyclomatic_complexity = []
        nloc = []
        token_count = []
        long_name = []
        length = []
        file_name = []

        i = lizard.analyze_file(files_dir + '/' + file)

        # code complexity is calculated on those files which have methods in large codes
        if len(i.function_list) != 0:

            for func in i.function_list:

                cyclomatic_complexity.append(func.__dict__['cyclomatic_complexity'])
                nloc.append(func.__dict__['nloc'])
                token_count.append(func.__dict__['token_count'])
                length.append(func.__dict__['length'])

            # lets create dataframe which stores method wise code complexity values
            df = pd.DataFrame({'cyclomatic_complexity': cyclomatic_complexity,
                               'nloc': nloc,
                               'token_count': token_count,
                               'length': length})

            # since we want to calculate code level cyclometric complexity, so we add method level complexities
            df_x = pd.DataFrame(df.sum(axis=0)).T
            df_x['file_name'] = [file]
            df_x['number_of_functions'] = df.shape[0]
            df_x['average_function_lenght'] = df['length'].mean()
            df_x['code_to_comment_ratio'] = (df_x['length'] - df_x['nloc']) / df_x['length']
            df_x['code_to_comment_ratio_percent'] = df_x['code_to_comment_ratio'] * 100
            df_x.drop(columns=['code_to_comment_ratio', 'nloc', 'token_count'], inplace=True)

            # print(df_x)
            # save values in .csv formar
            df_x.to_csv(path_to_save + file + '.csv')


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="usage: python main.py <arguments>")
    parser.add_argument("--files_dir", help="code files .py, .cpp, .rb, .c", default=None, required=True)
    parser.add_argument("--path_to_save", help="dir path to save results", default=None, required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(args)
    main(args.files_dir, args.path_to_save)
